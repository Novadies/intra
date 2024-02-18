import pandas as pd

from typing import List, Dict, Any

from django.db import transaction
from pydantic import ValidationError

from loader.models import TestModel, Aggregator
from logs.logger import log_apps


def read_excel__to_dict(file_path):
    """ На вход получаем адресс файла, а на выходе генератор словарей"""
    try:
        df = pd.read_excel(file_path)
        df.fillna(value='', inplace=True)
        data_dict = df.to_dict(orient='records')
        yield from data_dict[1:]               # если есть заголовок, убираем его
    except Exception as e:
        log_apps.warning(f"Ошибка чтения файла Excel: {e}")

def router(input_dict):
    result_dicts = {}
    # Получаем имена полей для каждой модели из класса Aggregator
    for instance_dict in Aggregator.__dict__.values():
        if isinstance(instance_dict, dict):
            model_class, validator = instance_dict.items()
            if hasattr(model_class, "_meta"):
                field_names = [field.name for field in model_class._meta.fields]
                result_dicts[instance_dict] = {key: value for key, value in input_dict.items() if key in field_names}
                yield from result_dicts


def validate_dict(list_dict):
    """ Генератор для валидации пайдэнтиком """
    key, data = list_dict.items()
    model, validator = key.items()
    for _dict in data:
        try:
            to_dict  = validator(**_dict)
            yield {model : to_dict.dict()}
        except ValidationError as e:
            log_apps.warning(f"При валидации данных произошло исключение {e}")


def entry_to_db(data_generator):
    """ Собираем N строк от генератора и записываем bulk_create-ом"""
    N = 10
    model, data_dict = data_generator.items()
    with transaction.atomic():
        try:
            while True:
                data = []
                for _ in range(N):  # использование спискового включения не выполняет сохранение после StopIteration
                    data.append(next(data_dict))
                objects_to_create(data, model)
        except StopIteration:
            if data:                # Если остались объекты после окончания генерации, добавляем их
                objects_to_create(data, model)

def objects_to_create(data, model):
    objects = [model(**item) for item in data]
    try:
        model.objects.bulk_create(objects)
    except Exception as e:
        log_apps.warning(f"При попытке сохранения данных произошло исключение {e}")