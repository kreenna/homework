import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def some_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_id",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("NOTFOUND", []),  # если state не указан
    ],
)
def test_filter_by_state(some_data: list, state: str, expected_id: str) -> None:
    filtered = filter_by_state(some_data, state)
    assert [item["id"] for item in filtered] == expected_id


@pytest.mark.parametrize(
    "data, descending, expected_order",
    [
        # тест по возрастанию
        (
            [{"date": "2022-01-01"}, {"date": "2021-01-01"}, {"date": "2023-01-01"}],
            False,
            [{"date": "2021-01-01"}, {"date": "2022-01-01"}, {"date": "2023-01-01"}],
        ),
        # тест по убыванию
        (
            [{"date": "2022-01-01"}, {"date": "2021-01-01"}, {"date": "2023-01-01"}],
            True,
            [{"date": "2023-01-01"}, {"date": "2022-01-01"}, {"date": "2021-01-01"}],
        ),
        # тест на одинаковые даты
        (
            [{"date": "2022-01-01"}, {"date": "2021-01-01"}, {"date": "2022-01-01"}],
            False,
            [{"date": "2021-01-01"}, {"date": "2022-01-01"}, {"date": "2022-01-01"}],
        ),
        # некорректные форматы дат
        ([{"date": "invalid-date"}], False, ""),
        ([{"date": None}], False, ""),
        ([{"date": ""}], False, ""),
    ],
)
def test_sort_by_date(data: list, descending: bool, expected_order: list) -> None:
    sorted_data = sort_by_date(data, descending)
    assert [item["date"] for item in sorted_data] == [item["date"] for item in expected_order]
