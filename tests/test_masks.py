import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_card, expected_output",
    [
        ("6757342342234326", "6757 34** **** 4326"),
        ("5632 1235 9835 1258", "5632 12** **** 1258"),
        ("", ""),  # пустая строка
        ("542", ""),  # короткая
        ("67890127467815673819837261414", "6789 01** **** 1414"),
    ],
)
def test_get_mask_card_number(input_card: str, expected_output: str) -> None:
    assert get_mask_card_number(input_card) == expected_output


@pytest.mark.parametrize(
    "input_account, expected_output",
    [
        ("84573627496038375638", "**5638"),
        ("7533 5121 5432", "**5432"),
        ("", ""),  # пустая строка
        ("12", ""),  # короткая
    ],
)
def test_get_mask_account(input_account: str, expected_output: str) -> None:
    assert get_mask_account(input_account) == expected_output
