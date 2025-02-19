import re
from collections import Counter
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


def filter_by_description(transactions: list, string: str) -> list:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    """

    # проверяем, что нужные аргументы присутствуют
    if transactions and string:
        sorted_transactions: list = []
        search_string = string.lower()

        for one in transactions:

            # ищем нужную строку в транзакции
            if re.search(search_string, one["description"].lower()):
                sorted_transactions.append(one)

            return sorted_transactions

    else:
        return []


def count_transactions_categories(transaction_data: list, categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """

    # извлекаем описания транзакций
    descriptions = [transaction["description"] for transaction in transaction_data]

    # подсчитываем количество вхождений каждого типа операции
    description_counts = Counter(descriptions)

    # формируем результат для заданных категорий
    result = {category: description_counts.get(category, 0) for category in categories}

    return result
