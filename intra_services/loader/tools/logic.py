from pathlib import Path
from typing import List, Dict, Any, BinaryIO, Optional

import pandas as pd
from django.contrib import messages
from tenacity import retry, stop_after_attempt, wait_fixed

from django.db import transaction

from logs.logger import log_apps

from loader.tasks import entry_to_db_task

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def save_file(_self: object, uploaded_files: BinaryIO) -> Optional[None]:
    """ Сохраняем файл на сервер и добавляем его адрес в бд, если сохранение успешно вызываем запись данных файла в бд
    Добавлен повтор при неудачном сохранении файла.
    """
    if uploaded_files:
        with transaction.atomic():
            # for uploaded_file in uploaded_files:
            upload_instance = _self.model(file_to_upload=uploaded_files, to_user=_self.request.user)
            upload_instance.save()
            path = Path(upload_instance.file_to_upload.path)
            if path.exists():
                # messages.add_message(_self.request, messages.INFO,
                #                      f"Успешная загрузка {upload_instance.file_to_upload.name} ",
                #                      fail_silently=True)

                # entry_to_db_task.delay(path)
                entry_to_db_task(path)
            else:
                log_apps.warning(f'Что-то пошло не так и {upload_instance.file_to_upload.name} не загружен на сервер.')
                raise FileNotFoundError(f'File {upload_instance.file_to_upload.name} does not exist')







# def save_in_session(model, form, name_in_session: str, checkbox_name='mail_checkbox'):
#     """ Сохранение в сессию значения из name_in_session, по этому ключу """
#     if model.request.session.get(name_in_session, None) is not (value := form.cleaned_data[checkbox_name]):
#         model.request.session[name_in_session] = value
#         ic(f'Данные сессии изменены.{checkbox_name} : {value}')
#
# def save_in_cookies(model, form, responses, name_in_cookie: str, checkbox_name='mail_checkbox'):
#     """ Сохранение в cookies значения из поля name_in_cookie, по этому ключу """
#     if model.request.COOKIES.get(name_in_cookie, None) is not (value := form.cleaned_data[checkbox_name]):
#         responses.set_cookie(name_in_cookie, value)
#         ic(f'Данные куки изменены.{checkbox_name} : {value}')
