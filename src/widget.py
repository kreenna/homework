from typing import Iterable, Optional

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_and_number: Optional[str]) -> str:
    """
    Возвращает строку с замаскированным номером карты или счета. Для карт и счетов используется свой тип маскировки.
    """
    name: Iterable[str] = []
    number: str = ""
    while card_and_number.split(" ")[0] == "Счет":
        for one in card_and_number.split(" "):
            if one.isdigit():
                number = one
        return "Счет " + get_mask_account(number)
    for one in card_and_number.split(" "):
        if one.isalpha():
            name.append(one)
        elif one.isdigit():
            number = one
    return " ".join(name) + " " + get_mask_card_number(number)


def get_date(date: Optional[int]) -> str:
    pass
