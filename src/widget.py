from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_and_number: str) -> str:
    """
    Возвращает строку с замаскированным номером карты или счета. Для карт и счетов используется свой тип маскировки.
    """

    if card_and_number is None:
        return ""

    name: list = []
    number: list = []
    card_and_number_list: list = card_and_number.split(" ")

    while card_and_number_list[0] == "Счет":
        if len("".join(card_and_number_list[1:])) > 10:
            for one in card_and_number_list:
                if one.isdigit():
                    number.append(one)
            return "Счет " + get_mask_account("".join(number))
        else:
            return ""

    for one in card_and_number.split(" "):
        if one.isalpha():
            name.append(one)
        elif one.isdigit():
            number.append(one)

    if len("".join(number)) > 10:
        return " ".join(name) + " " + get_mask_card_number("".join(number))
    else:
        return ""


def get_date(date: str) -> str:
    """
    Принимает дату, возвращает строку в формате "ДД.ММ.ГГГГ"
    """

    if date is None or date == "":
        return ""

    preformat_date: str = date.split("T")[0]
    format_date: list = preformat_date.split("-")[::-1]
    if "".join(format_date).isdigit():
        return ".".join(format_date)
    else:
        return ""
