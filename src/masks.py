import logging
import os

from config import PATH_HOME

# настройки логгера
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename=os.path.join(PATH_HOME, "logs/masks.log"),  # запись логов в файл
    filemode="w",
    encoding="utf-8",
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
