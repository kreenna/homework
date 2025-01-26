from typing import Iterator, Union


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """
    Функция, которая выводит транзакции по заданной валюте.
    """

    for one in transactions:
        if one["operationAmount"]["currency"]["code"] == currency:
            yield one


def transaction_descriptions(transactions: list) -> Iterator:
    """
    Возвращает описание каждой операции по очереди.
    """
    for one in transactions:
        yield one["description"]


def card_number_generator(start: Union[str, int], stop: Union[str, int]) -> Iterator:
    """
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    if start and stop:
        start_str = str(start)
        stop_str = str(stop)
        if not start_str.isdigit() or not stop_str.isdigit():
            yield None

        else:
            if int(start_str) < 1 or int(stop_str) > 9999999999999999:
                yield None

            else:
                for number in range(int(start), int(stop_str) + 1):
                    card_number = str(number).zfill(16)
                    formatted_card_number = (
                        f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
                    )
                    yield formatted_card_number

    else:
        yield None
