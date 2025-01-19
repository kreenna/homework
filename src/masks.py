def get_mask_card_number(number: str) -> str:
    """
       Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX, где X
    — это цифра номера.
    """
    card_number = number.replace(" ", "")
    if len(card_number) >= 10:
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return ""


def get_mask_account(number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — это цифра номера.
    """
    card_number = number.replace(" ", "")
    if len(card_number) >= 10:
        return "**" + number[-4:]
    return ""
