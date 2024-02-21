
from .tools.for_save_to_db import read_excel__to_dict, validate_dict, entry_to_db, router, gen_report

from logs.logger import log_apps


def entry_to_db_task(file_path):  # задача для селери как-то так выглядит
    """ Последовательно вызываем функции для записи на сервер.
    Сначала получаем генератор словарей, который валидирует соответсвие полей и валидирующий значения,
    entry_to_db агрегирует данные от генератора и записывает в бд bulk_create-ом."""
    """ Если исходить из того что это будет на селери, то все ошибки придут сюда а не в save_file, вызывающийся во form_valid  FileLoader """
    # try:
    data = read_excel__to_dict(file_path, engine='Pandas')
    router_data = router(data, is_validate=True, check_compliance=True)
    entry_to_db(router_data, N=10, similar_batch_size=999)
    # except Exception:
    #     log_apps.warning(f'Как то отправить получателю, что ничего не вышло')


