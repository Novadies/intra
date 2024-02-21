import pandas as p

from contextlib import suppress
from dataclasses import asdict
from typing import List, Dict, Any, Generator
from pydantic import ValidationError
from itertools import count

from django.db import transaction

from loader.models import aggregator, TestModel
from logs.logger import log_apps


def read_excel__to_dict(file_path, engine) -> Generator:
    """ На вход получаем адресс файла, а на выходе генератор словарей"""
    # try:
        # match engine:               # 3.10
        #     case "Pandas":
        #         import pandas as p
        #     case "Polars":
        #         import polars as p
        #         p.default_options().na = ''
        # если указывать дополнительные параметры совместимость нарушиться, и надо будет разбивать на отдельные функции
    """ df это генератор """
    df = p.read_excel(file_path)
    # with suppress(Exception):
    df.fillna(value='', inplace=True)
    row_list_dict = df.to_dict(orient='records')
    yield from row_list_dict[1:]  # если есть заголовок, убираем его
    # except Exception as e:
    #     log_apps.warning(f"Ошибка чтения файла Excel: {e}")
    #     raise Exception(f'Ошибка отправлена вверх по стеку')

def router(generator: Generator, is_validate: bool = True, check_compliance: bool = False) -> Generator:
    """ разделяем список генераторов по моделям """
    # Получаем имена полей для каждой модели из класса Aggregator
    for item in generator:
        result_row = []
        for instance in asdict(aggregator).values():
            model, validator = instance
            if hasattr(model, "_meta"):
                model_fields = [field.name for field in model._meta.fields]
                # if check_compliance:  # todo возможно переместить в другое место
                #     check_fields(model_fields, validator)  # todo сделать проверку соответствия полей model и validator
                check_fields(model_fields, validator)
                data = {model: {key: value for key, value in item.items() if key in model_fields}}
                data = validate(data, validator) if is_validate else data
                result_row.append(data)
        yield result_row

def check_fields(model, validator):
    print(list(validator.__annotations__))

    if False:
        raise Exception(f'Не соответствие между существующими полями модели(в количестве?) {model} и полями его валидатора {validator}')


def validate(item, validator):  # аннотацию
    """ Валидация данных перед генерацией значения """
    (model, data), = item.items()
    val_data = validator.model_validate(data)
    return {model: val_data.dict()}


def entry_to_db(generator, N=None, similar_batch_size=None):
    """ Собираем N строк от генератора и записываем bulk_create-ом"""
    scope = range(N) if N is not None and isinstance(N, int) else count(0)
    #with transaction.atomic():
    try:
        while True:
            if_break = False    # флаг для break
            data_dict = {}
            for i in scope:
                items = next(generator)
                if items:
                    for item in items:
                        (model, model_data), = item.items()
                        if model not in data_dict:
                            data_dict[model] = []  # Если модель не встречалась ранее, создаем пустой список для нее
                        data_dict[model].append(model_data)
                        if similar_batch_size and i*len(model_data) > similar_batch_size:
                            if_break = True
                if if_break:    # выход из цикла for если значений больше чем similar_batch_size
                    break
            ic(data_dict)
            #objects_to_create(data_dict)    # записываем в бд в конце каждой итерации while
    except StopIteration:
        if data_dict:  # Если остались объекты после окончания генерации, добавляем их
            #objects_to_create(data_dict)
            ic(data_dict)



def objects_to_create(_dict):
    """  """
    for model, list_data in _dict.items():
    #     try:
        objects = [model(**item) for item in list_data]
        # objects = (model(item) for item in list_data)
        #ic(objects)
        #TestModel.objects.create(**{'numberlist': 1})
        model.objects.bulk_create(objects)
        # model.objects.bulk_create([
        #     #TestModel(**{'numberlist': 1, 'id_fabrics': '', 'id_work': 36, 'id_insta': '', 'id_contract': 'ООО &quot;АЛКИ-УРАЛ&quot;', 'id_execut': 'Гильванов С.М.', 'id_object': '40DB-412', 'id_cat': '', 'id_med': 'углеводороды'})])
        #     model(numberlist=1, id_fabrics='', id_work=36, id_insta='')])
    #     except Exception as e:
    #         log_apps.warning(f"При попытке сохранения данных произошло исключение {e}")
    #         raise Exception(f'Ошибка отправлена вверх по стеку')




def validate_dict(generator: Generator) -> Generator:  # не используется, вместо него валидация на месте validate()
    """ Генератор для валидации пайдэнтиком """
    try:
        for items in generator:
            result_row = []
            for item in items:
                (_tuple, data), = item.items()
                model, validator = _tuple
                val_data = validator.model_validate(data)
                result_row.append({model: val_data.dict()})
            yield result_row
    except ValidationError as e:
        log_apps.warning(f"При валидации данных произошло исключение {e}")
        raise Exception(f'Ошибка отправлена вверх по стеку')


def gen_report(gen: Generator) -> Generator:
    """ Возвращает идентичный входному генератор, выводя значения входного"""
    return ((ic(i), i)[-1] for i in gen)
