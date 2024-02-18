
from .tools.for_save_to_db import read_excel__to_dict, validate_dict, entry_to_db

from logs.logger import log_apps


def entry_to_db_task(file_path):  # задача для селери как-то так выглядит
    """ Последовательно вызываем функции для записи на сервер.
    Сначала получаем генератор словарей,
    потом генератор валидирующий значения,
    наконец entry_to_db агрегирует данные от генератора и запись в бд bulk_create-ом.
    """
    data = read_excel__to_dict(file_path)
    v_data = validate_dict(data)
    entry_to_db(v_data)


