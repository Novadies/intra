# pytest C:\Users\RysukAO\PycharmProjects\intra\intra_services\users\tool\test_copy.py -s

import pytest
import arrow

from users.tool.copy import honeymoneymany


@pytest.fixture()
def data():
    rate = 100
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
    return rate, koefficient


@pytest.mark.parametrize('report_card, expected_result',
                         [
                             ({arrow.get(2024, 3, 12).date(): 6},
                              600),
                             ({arrow.get(2024, 3, 13).date(): 8},
                              800),
                             ({arrow.get(2024, 3, 14).date(): 10},
                              1100),
                             ({arrow.get(2024, 3, 15).date(): 12},
                              1500),
                             ({arrow.get(2024, 3, 16).date(): 11},
                              1300),
                             ({arrow.get(2024, 3, 17).date(): 9},
                              950),
                         ]
                         )
def test_honeymoneymany2(data, report_card, expected_result):
    result = honeymoneymany(*data, report_card)
    assert pytest.approx(result[0]) == float(expected_result)
