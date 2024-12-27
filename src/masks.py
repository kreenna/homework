from typing import Optional


def get_mask_card_number(number: Optional[int]) -> str:
    """
       Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX, где X
    — это цифра номера.
    """
    card_number = str(number)
    return card_number[0:4] + " " + card_number[5:7] + "** **** " + card_number[-4:]


def get_mask_account(number: Optional[int]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — это цифра номера.
    """
    account_number = str(number)
    return "**" + account_number[-4:]
