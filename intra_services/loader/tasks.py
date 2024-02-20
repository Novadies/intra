
from .tools.for_save_to_db import read_excel__to_dict, validate_dict, entry_to_db, router, gen_report

from logs.logger import log_apps


def entry_to_db_task(file_path):  # задача для селери как-то так выглядит
    """ Последовательно вызываем функции для записи на сервер.
    Сначала получаем генератор словарей,
    потом генератор валидирующий значения,
    наконец entry_to_db агрегирует данные от генератора и запись в бд bulk_create-ом.
    """
    data = read_excel__to_dict(file_path, engine='Pandas')
    router_data = router(data)
    v_data = validate_dict(router_data)
    # v = gen_report(v_data)
    entry_to_db(v_data, N=10)



