from .models import aggregator
from .tools.save_to_db_class import read_excel__to_dict, entry_to_db, router, DB_ExcelEntry

from logs.logger import log_apps


# def entry_to_db_task(file_path):  # задача для селери как-то так выглядит
#     """ Последовательно вызываем функции для записи на сервер.
#     Сначала получаем генератор словарей, который валидирует соответсвие полей и валидирующий значения,
#     entry_to_db агрегирует данные от генератора и записывает в бд bulk_create-ом."""
#     """ Если исходить из того что это будет на селери, то все ошибки придут сюда а не в save_file, вызывающийся во form_valid  FileLoader """
#     try:
#         data = read_excel__to_dict(file_path, engine='Pandas')
#         router_data = router(data, is_validate=True, check_compliance=False)
#         entry_to_db(router_data, N=25, similar_batch_size=999)
#     except Exception as e:
#         log_apps.warning(f'Как то отправить получателю, что ничего не вышло', exc_info=True)

def entry_to_db_task_Class_version(upload_instance, file_path, instance_DB_ExcelEntry):  # задача для селери как-то так выглядит
    """ Последовательно вызываем функции для записи на сервер.
    Сначала получаем генератор словарей, который валидирует соответсвие полей и валидирующий значения,
    entry_to_db агрегирует данные от генератора и записывает в бд bulk_create-ом."""
    """ Если исходить из того что это будет на селери, то все ошибки придут сюда а не в save_file, вызывающийся во form_valid  FileLoader """
    try:
        # вместо save_class можно использовать экземпляр instance_DB_ExcelEntry, который передаётся через представление
        if instance_DB_ExcelEntry:                        # передаём агрументы, которые нельзя было передать изначально
            instance_DB_ExcelEntry.set_args(upload_instance=upload_instance, file_path=file_path)
        else:
            print('ВНИМАНИЕ! ДЛЯ ЗАПИСИ ИСПОЛЬЗУЕТСЯ ТЕСТОВАЯ МОДЕЛЬ!')
        save_class = instance_DB_ExcelEntry or DB_ExcelEntry(
            aggregator=aggregator,
            upload_instance=upload_instance,
            file_path=file_path,
            engine="Pandas",
            is_validate=True,
            check_compliance=False,
            N=10,
            similar_batch_size=999,
            header=True
        )

        data = save_class.read_excel__to_dict()
        router_data = save_class.router(data)
        save_class.entry_to_db(router_data)
    except Exception as e:
        log_apps.warning(f'Как то отправить получателю, что ничего не вышло', exc_info=True)
