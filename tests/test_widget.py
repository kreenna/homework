import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158 3007 3472 6758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831 9824 7673 7658", "Visa Classic 6831 98** **** 7658"),
        ("Visa 568", ""),
        ("Счет", ""),
        ("", ""),
        (None, ""),
    ],
)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-01-01T00:00:00.000000", "01.01.2021"),
        ("invalid-date", ""),
        ("", ""),
    ],
)
def test_get_data(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output
