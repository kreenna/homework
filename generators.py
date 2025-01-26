from typing import Iterator

def filter_by_currency(transactions: list, currency) -> Iterator:
    """
    Функция, которая выводит транзакции по заданной валюте.
    """

    for one in transactions:
        if one["operationAmount"]["currency"]["code"] == currency:
            yield one

def transaction_descriptions(transactions) -> list:
    pass

def card_number_generator():
    pass
