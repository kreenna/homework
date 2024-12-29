def get_mask_card_number(number: str) -> str:
    """
       Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX, где X
    — это цифра номера.
    """
    return number[0:4] + " " + number[5:7] + "** **** " + number[-4:]


def get_mask_account(number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — это цифра номера.
    """
    return "**" + number[-4:]
