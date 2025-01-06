from typing import Optional


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


def sort_by_date(data: list, reverse_option: Optional[bool] = True) -> list:
    """
    Функция, принимающая список словарей и необязательный параметр, задающий порядок сортировки (изначально по убыванию).
    Возвращает отсортированный список словарей.
    """
    sorted_data: list = sorted(data, key=lambda x: x["date"], reverse=reverse_option)
    return sorted_data
