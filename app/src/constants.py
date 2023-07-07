employers_dict = {
    'Yandex': 1740,
    'VK': 15478,
    'Rambler': 8620,
    'Sber': 3529,
    'Tinkoff': 78638,
    'QSOFT': 4006,
    'Maks': 4504679,
    'NodaSoft': 561525,
    '2ГИС': 64174,
    'Рут Код': 8642172,
    'Eqvanta': 3785152,
    'Beeline': 4934,
    'MindBox': 205152,
    'MTS': 3776,
    'ОТП Банк': 4394
}

employers_list = [1740, 15478, 8620, 3529, 78638, 4006, 4504679, 561525, 64174, 8642172, 3785152, 4934, 205152, 3776, 4394]


def db_dict() -> dict:
    return {"host": "localhost", "database": "cw_5", "user": "postgres", "password": "qadratura"}
