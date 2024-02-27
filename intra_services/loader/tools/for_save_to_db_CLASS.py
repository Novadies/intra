import pandas as p

from contextlib import suppress
from typing import List, Dict, Any, Generator, Type, Literal, Optional, Union

from django.db.models import Model
from pydantic import ValidationError, BaseModel
from itertools import count

from django.db import transaction

from logs.logger import log_apps


class DB_ExcelEntry:
    """ Базовый класс для записи из эксель.
        objects_to_create() требует переопределения в случае работы с разными моделями
    """

    def __init__(self,
                 aggregator=None,
                 upload_instance=None,
                 file_path=None,
                 engine: Literal["Pandas", "Polars"] = "Pandas",
                 is_validate: bool = True,
                 check_compliance: bool = True,
                 N: Optional[int] = 10,
                 similar_batch_size: Optional[int] = 999,
                 sheet: Union[str, None] = None,
                 header: bool = True,
                 value: str = '',
                 ):
        self.aggregator = aggregator
        self.upload_instance = upload_instance
        self.file_path = file_path
        self.engine = engine
        self.is_validate = is_validate
        self.check_compliance = check_compliance
        self.N = N
        self.similar_batch_size = similar_batch_size
        self.sheet = sheet  # todo пока не используется/ нужно передавать имя страницы
        self.header = header
        self.value = value

    def set_args(self, upload_instance, file_path):
        """ Что бы определить аргументы позже """
        self.upload_instance = upload_instance
        self.file_path = file_path

    def read_excel__to_dict(self, orient='records', inplace=True) -> Generator:
        """ На вход получаем адрес файла, а на выходе генератор из словарей"""
        # match engine:               # 3.10
        #     case "Pandas":
        #         import pandas as p
        #     case "Polars":
        #         import polars as p
        #         p.default_options().na = self.value

        """ df это генератор """
        try:
            df = p.read_excel(self.file_path)
        except Exception:
            df = p.read_csv(self.file_path)
        with suppress(Exception):
            df.fillna(value=self.value, inplace=inplace)  # указываем значения в пустых ячейках
        row_list_dict = df.to_dict(orient=orient)

        yield from row_list_dict[1:] if self.header else row_list_dict  # если есть заголовок, убираем его

    def router(self, generator: Generator) -> Generator:
        """ Разделяем генератор по структурным частям, в соответствии с моделями, то есть читаем его, обрабатываем, передаём дальше
        Так же ранее ключи в генераторе были кортежем(model, validator), а стали просто model.
        """
        for item in generator:
            result_row = []
            for instance in self.aggregator.mytuple:  # Получаем кортежи (модель - валидатор) из класса Aggregator
                model, validator = instance
                model_fields = [field for field in model._meta.fields]
                if self.check_compliance:  # проверка полей модели и валидатора
                    self.check_fields(model_fields, validator)
                data = {
                    model: {key: value for key, value in item.items() if key in [field.name for field in model_fields]}}
                data = self.validate(data, validator) if self.is_validate else data  # валидация пайдентиком
                result_row.append(data)
            self.check_compliance = False  # для того что бы не проверять по десять раз одно и тоже
            yield result_row

    def entry_to_db(self, generator: Generator) -> None:
        """ Собираем N строк от генератора и записываем bulk_create-ом"""
        scope = range(self.N) if self.N is not None and isinstance(self.N, int) else count(0)
        with transaction.atomic():
            try:
                while True:
                    if_break = False  # флаг для break
                    data_dict = {}
                    for i in scope:
                        items = next(generator)  # итерация по генератору
                        if items:
                            for item in items:  # итерация по 'моделям'
                                (model, model_data), = item.items()
                                if model not in data_dict:
                                    data_dict[
                                        model] = []  # Если модель не встречалась ранее, создаем пустой список для нее
                                data_dict[model].append(model_data)
                                if self.similar_batch_size and i * len(model_data) > self.similar_batch_size:
                                    if_break = True
                        if if_break:  # выход из цикла for если значений больше чем similar_batch_size
                            break
                    self.objects_to_create(data_dict)  # записываем в бд в конце каждой итерации while
            except StopIteration:
                self.upload_instance.db_record = self.upload_instance.STATUS.published
                self.upload_instance.save()  # изменяем статус загруженного файла
                if data_dict:  # Если остались объекты после окончания генерации, записываем их
                    self.objects_to_create(data_dict)

    def objects_to_create(self, _dict: dict) -> None:
        # fixme в текущей реализации нет связей между собою между загружаемыми моделями, так как связи могут быть разными,
        # fixme то для разных вариантов загружаемых моделей нужно переопределять objects_to_create() и не забывать создавать связи в моделях
        """ запись в бд с помощью  bulk_create.
        Данный метод вероятно придётся переопределять если загружать другие файлы
        """
        for model, list_data in _dict.items():
            objects = (model(**item, to_uploader=self.upload_instance, to_user=self.upload_instance.to_user)
                       for item in list_data)  # добавлена связь на модель загрузчика и юзера
            model.objects.bulk_create(objects)

    @staticmethod
    def check_fields(model_fields: List[Model], validator: Type[BaseModel]):
        """ Поля модели и поля его валидатора должны совпадать """

        def exclude(input_fields: List[Model], *args: str) -> list:
            """ Получение полей из модели исключая определенные """
            return [field.name for field in input_fields
                    if not any([field.one_to_one, field.many_to_many, field.many_to_one, field.one_to_many])
                    and field.name not in ["id", *args]]

        mod_fields = exclude(model_fields)
        val_fields = list(validator.model_fields)
        if mod_fields != val_fields:
            raise Exception(
                f'Не соответствие между существующими полями модели {mod_fields} и полями его валидатора {val_fields}')

    @staticmethod
    def validate(item: dict, validator: Type[BaseModel]) -> dict:
        """ Валидация данных перед генерацией значения """
        (model, data), = item.items()
        val_data = validator.model_validate(data)
        return {model: val_data.dict()}


########################################################################################################################
########################################################################################################################
########################################################################################################################
# Канонический вариант обычных функций

def read_excel__to_dict(file_path, engine: Literal["Pandas", "Polars"]) -> Generator:
    """ На вход получаем адрес файла, а на выходе генератор из словарей"""
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
    df.fillna(value='', inplace=True)  # указываем значения в пустых ячейках
    row_list_dict = df.to_dict(orient='records')
    yield from row_list_dict[1:]


def router(generator: Generator, is_validate: bool = True, check_compliance: bool = False) -> Generator:
    """ разделяем генератор по структурным частям, в соответствии с моделями, то есть читаем его, обрабатываем, передаём дальше
    Так же ранее ключи в генераторе были кортежем(model, validator), а стали просто model.
    """
    from loader.models import aggregator  # что б не было конфликта имён внутри этоого модуля

    for item in generator:
        result_row = []
        for instance in aggregator.mytuple:  # Получаем кортежи (модель - валидатор) из класса Aggregator
            model, validator = instance
            model_fields = [field for field in model._meta.fields]
            if check_compliance:  # проверка полей модели и валидатора
                check_fields(model_fields, validator)
            data = {model: {key: value for key, value in item.items() if key in [field.name for field in model_fields]}}
            data = validate(data, validator) if is_validate else data  # валидация пайдентиком
            result_row.append(data)
        check_compliance = False  # для того что бы не проверять по десять раз одно и тоже
        yield result_row


def check_fields(model_fields: List[Model], validator: Type[BaseModel]):
    """ Поля модели и поля его валидатора должны совпадать """
    mod_fields = exclude(model_fields)
    val_fields = list(validator.model_fields)
    if mod_fields != val_fields:
        raise Exception(
            f'Не соответствие между существующими полями модели {mod_fields} и полями его валидатора {val_fields}')


def exclude(input_fields: List[Model], *args: str) -> list:
    """ Получение полей из модели исключая определенные """
    return [field.name for field in input_fields
            if not any([field.one_to_one, field.many_to_many, field.many_to_one, field.one_to_many])
            or field.name not in ["id", *args]]


def validate(item: dict, validator: Type[BaseModel]) -> dict:
    """ Валидация данных перед генерацией значения """
    (model, data), = item.items()
    val_data = validator.model_validate(data)
    return {model: val_data.dict()}


def entry_to_db(generator: Generator, N: Optional[int] = None, similar_batch_size: Optional[int] = None) -> None:
    """ Собираем N строк от генератора и записываем bulk_create-ом"""
    scope = range(N) if N is not None and isinstance(N, int) else count(0)
    with transaction.atomic():
        try:
            while True:
                if_break = False  # флаг для break
                data_dict = {}
                for i in scope:
                    items = next(generator)  # итерация по генератору
                    if items:
                        for item in items:  # итерация по 'моделям'
                            (model, model_data), = item.items()
                            if model not in data_dict:
                                data_dict[model] = []  # Если модель не встречалась ранее, создаем пустой список для нее
                            data_dict[model].append(model_data)
                            if similar_batch_size and i * len(model_data) > similar_batch_size:
                                if_break = True
                    if if_break:  # выход из цикла for если значений больше чем similar_batch_size
                        break
                objects_to_create(data_dict)  # записываем в бд в конце каждой итерации while
        except StopIteration:
            if data_dict:  # Если остались объекты после окончания генерации, записываем их
                objects_to_create(data_dict)


def objects_to_create(_dict: dict) -> None:
    """ запись в бд с помощью  bulk_create"""
    for model, list_data in _dict.items():
        objects = (model(**item) for item in list_data)
        model.objects.bulk_create(objects)


########################################################################################################################

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
