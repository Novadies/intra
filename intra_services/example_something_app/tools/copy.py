from typing import Tuple, List, Union, Any, Dict

import arrow
import httpx
import json

from django.conf import settings

from logs.logger import log_apps

koefficient = {
    'shift': {
        'day': 1,
        'night': 1.2,
    },
    'overtime': {
        'zero': 1,
        'two': 1.5,
        'more_two': 2,
        'holiday': 2
    }
}
report_card = {arrow.get(2024, 3, 12).date(): 6,
               arrow.get(2024, 3, 13).date(): 8,
               arrow.get(2024, 3, 14).date(): 10,
               arrow.get(2024, 3, 15).date(): 12,
               arrow.get(2024, 3, 16).date(): 11,
               arrow.get(2024, 3, 17).date(): 9,
               }

rate = 250

def holiday(year):
    """ получаем список из праздничных и предпраздничных дней, остальные рабочие """
    url = f'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant{year}.json'
    file_path = settings.MEDIA_URL/ 'uploads' / f'holidays_and_preholidays_out_consultant_{year}.json'
    """ пробуем получить файл с сервера """
    try:
        with open(file_path, 'r') as file:
            cal = json.load(file)
        return cal.get("holidays", []), cal.get("preholidays", [])
    except FileNotFoundError:
        log_apps.info(f"Файл {file_path} не найден.")
    except json.JSONDecodeError as e:
        log_apps.warning(f"Ошибка при декодировании JSON: {e}")
    """ если его нет, пробуем получить файл с сайта, и сохранить его """
    try:
        r = httpx.get(url).raise_for_status()
        cal = r.json()
        with open(file_path, 'wb') as f:
            json.dump(cal, f)
        return cal.get("holidays", None), cal.get("preholidays", None)
    except httpx.HTTPError as e:
        log_apps.warning(f"Ошибка HTTP: {e}")
    return [], []

def honeymoneymany(rate: int, koef: dict, report_card: dict, base='day', pre_hol=True)-> Tuple[
    List[Union[int, Any]], Dict[Any, Union[int, Any]]]:
    """ Сравниваем дни с праздничными, получаем на выходе список из денег за смену или словарь день: деньги
    pre_hol флаг показывающий учитывать ли предпраздничные дни
    """
    money_dict = {}
    money = []
    year = '2024'  # todo год создать динамически из report_card
    # todo holidays, preholidays = holiday(year) так как календарь общий для всех, то он должен быть вынесен из функции
    holidays, preholidays = holiday(year)
    if not holidays:
        log_apps.warning(f"Праздничные и выходные дни не загружены!")
    for day, hours in report_card.items():
        if day in holidays:
            print(day, holidays)
            m = hours * rate * koef['shift'][base] * koef['overtime']['holiday']
            money_dict[day] = m
            money.append(m)
        else:
            shift = 7 if pre_hol and day in preholidays else 8
            hrs = min(hours, shift)
            ov1 = max(min(hours - shift, 2), 0)
            ov2 = max(hours - (shift+2), 0)
            print(hrs, ov1, ov2)
            m = (
                    hrs * rate * koef['shift'][base] * koef['overtime']['zero'] +
                    ov1 * rate * koef['shift'][base] * koef['overtime']['two'] +
                    ov2 * rate * koef['shift'][base] * koef['overtime']['more_two']
            )
            money_dict[day] = m
            money.append(m)
    return money, money_dict

honeymoneymany(rate, koefficient, report_card, base='day')




