from typing import Union

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected_output",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("NONE", []),
        ("", []),
        (None, []),  # нет валюты
    ],
)
def test_filter_by_currency(transactions: list, currency: str, expected_output: list) -> None:
    generator = filter_by_currency(transactions, currency)
    gotten_ids = [item["id"] for item in generator]
    assert gotten_ids == expected_output


@pytest.fixture
def empty() -> list:
    return []


@pytest.mark.parametrize(
    "currency, expected_output",
    [
        ("USD", []),
    ],
)
def test_filter_by_currency_empty(empty: list, currency: str, expected_output: list) -> None:  # нет транзакций
    assert list(filter_by_currency(empty, currency)) == expected_output


@pytest.mark.parametrize(
    "transaction, expected_output",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"],
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            ["Перевод организации"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transaction: list, expected_output: list) -> None:
    generator = transaction_descriptions(transaction)
    assert list(generator) == expected_output


@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10000, 10002, ["0000 0000 0001 0000", "0000 0000 0001 0001", "0000 0000 0001 0002"]),
        ("5", "7", ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"]),
    ],
)
def test_card_number_generator(start: Union[str, int], stop: Union[str, int], expected_output: list) -> None:
    generator = card_number_generator(start, stop)
    assert list(generator) == expected_output


@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (9999999999999998, 10000000000000000, [None]),
        ("y4o", "y7o", [None]),
        (0, 0, [None]),
        (None, None, [None]),
    ],
)
def test_card_number_generator_invalid(start: Union[str, int], stop: Union[str, int], expected_output: list) -> None:
    generator = card_number_generator(start, stop)
    assert list(generator) == expected_output
