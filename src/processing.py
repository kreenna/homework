from typing import Optional

from src.widget import get_date


def filter_by_state(data: list, state: Optional[str] = "EXECUTED") -> list:
    """
    Функция, которая принимает список словарей и опциональное значение для ключа state.
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """

    needed_data: list = []
    for one in data:
        if one["state"] == state:
            needed_data.append(one)
    return needed_data


def sort_by_date(data: list, reverse_option: bool = True) -> list:
    """
    Функция, принимающая список словарей и опциональный параметр, задающий порядок сортировки (изначально по убыванию).
    Возвращает отсортированный список словарей.
    """

    date: str = get_date(data[0]["date"])
    if date == "":
        return []

    sorted_data: list = sorted(data, key=lambda x: x["date"], reverse=reverse_option)
    return sorted_data
