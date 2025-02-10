import logging

# настройки логгера
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="../logs/masks.log",  # запись логов в файл
    filemode="w",
)  # перезапись файла при каждом запуске


def get_mask_card_number(number: str) -> str:
    """
       Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX, где X
    — это цифра номера.
    """
    card_number = number.replace(" ", "")

    logging.info(f"Проверяем, что номер карты {card_number} не короче 10 символов.")
    if len(card_number) >= 10:

        logging.info(f"Номер карты {card_number} прошел проверку.")
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    logging.info(f"Номер карты {card_number} слишком короткий.")
    return ""


def get_mask_account(number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — это цифра номера.
    """
    card_number = number.replace(" ", "")

    logging.info(f"Проверяем, что номер счета {card_number} не короче 10 символов.")
    if len(card_number) >= 10:

        logging.info(f"Номер счета {card_number} прошел проверку.")
        return "**" + number[-4:]

    logging.info(f"Номер счета {card_number} слишком короткий.")
    return ""


print(get_mask_card_number("432465278568321424"))
print(get_mask_account("532465378154632857318"))
