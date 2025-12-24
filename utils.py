# #TG-RECAP (https://mrkrk.me/projects/tg-recap)
# Copyright (C) 2025 Viktor K.

import os
import sys

MONTHS_RU = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]


def format_day_ru(day_str):
    y, m, d = day_str.split("-")
    return f"{int(d)} {MONTHS_RU[int(m) - 1]}"


def inflect_with_num(number, forms):
    units = number % 10
    tens = number % 100 - units
    if tens == 10 or units >= 5 or units == 0:
        needed_form = 1
    elif units > 1:
        needed_form = 2
    else:
        needed_form = 0
    return forms[needed_form]


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
