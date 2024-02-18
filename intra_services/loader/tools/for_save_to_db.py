import pandas as pd

from typing import List, Dict, Any

from django.db import transaction
from pydantic import ValidationError

from loader.models import TestModel
from loader.validators import Item
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

def validate_dict(list_dict: List[Dict[str, Any]]):
    """ Генератор для валидации пайдэнтиком """
    for _dict in list_dict:
        try:
            to_dict  = Item(**_dict)
            yield to_dict.dict()
        except ValidationError as e:
            log_apps.warning(f"При валидации данных произошло исключение {e}")


def entry_to_db(data_generator):
    """ Собираем N строк от генератора и записываем bulk_create-ом"""
    N = 10
    with transaction.atomic():
        try:
            while True:
                data = []
                for _ in range(N):  # использование спискового включения не выполняет сохранение после StopIteration
                    data.append(next(data_generator))
                objects_to_create(data, TestModel)
        except StopIteration:
            if data:                # Если остались объекты после окончания генерации, добавляем их
                objects_to_create(data, TestModel)

def objects_to_create(data, model):
    objects = [model(**item) for item in data]
    try:
        model.objects.bulk_create(objects)
    except Exception as e:
        log_apps.warning(f"При попытке сохранения данных произошло исключение {e}")