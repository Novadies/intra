
import pandas as p

from contextlib import suppress
from dataclasses import asdict
from typing import List, Dict, Any, Generator
from pydantic import ValidationError
from itertools import count

from django.db import transaction

from loader.models import aggregator
from logs.logger import log_apps


def read_excel__to_dict(file_path, engine) -> Generator:
    """ На вход получаем адресс файла, а на выходе генератор словарей"""
    try:
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
    except Exception as e:
        log_apps.warning(f"Ошибка чтения файла Excel: {e}")


def router(generator: Generator) -> Generator:
    """ разделяем список генераторов по моделям """
    # Получаем имена полей для каждой модели из класса Aggregator
    for item in generator:
        result_row = []
        for instance in asdict(aggregator).values():
            model_class, validator = instance
            if hasattr(model_class, "_meta"):
                field_names = [field.name for field in model_class._meta.fields]
                result_row.append({instance: {key: value for key, value in item.items() if key in field_names}})
        yield result_row


def validate_dict(generator: Generator) -> Generator:
    """ Генератор для валидации пайдэнтиком """
    try:
        for items in generator:
            result_row = []
            for item in items:
                (_tuple, data), = item.items()
                model, validator = _tuple
                # val_data = validator.model_validate(data)  # добавил model_validate
                # data = val_data.dict()
                data = data
                result_row.append({model: data})
            yield result_row
    except ValidationError as e:
        log_apps.warning(f"При валидации данных произошло исключение {e}")


def entry_to_db(generator, N=None):
    """ Собираем N строк от генератора и записываем bulk_create-ом"""
    scope = (lambda N: None if N is None else range(N) if isinstance(N, int) else None)(N) or count(0)
    with transaction.atomic():
        try:
            while True:
                accumulated_data = []
                for _ in scope:
                    items = next(generator)
                    data = {}
                    if items:
                        for item in items:
                            (model, list_data), = item.items()
                            data[model] = list_data
                        accumulated_data.append(data)
                ic(accumulated_data)

                # objects_to_create(model, data)
        except StopIteration:
            if accumulated_data:  # Если остались объекты после окончания генерации, добавляем их
                # objects_to_create(model, data)
                print(accumulated_data)


def objects_to_create(model, data):
    objects = [model(**item) for item in data]
    try:
        model.objects.bulk_create(objects)
    except Exception as e:
        log_apps.warning(f"При попытке сохранения данных произошло исключение {e}")


def gen_report(gen: Generator) -> Generator:
    """ Возвращает идентичный входному генератор, выводя значения входного"""
    return ((ic(i), i)[-1] for i in gen)
