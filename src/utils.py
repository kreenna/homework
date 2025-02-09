import json
import os

from config import PATH_HOME


def get_transactions(path_name: str) -> list:
    """
    Принимает путь до JSON-файла и возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    try:
        with open(os.path.join(PATH_HOME, path_name), "r", encoding="utf-8") as file:
            converted_data: list = json.load(file)

        if not isinstance(converted_data, list):
            return []

    except Exception:
        return []

    return converted_data


def get_ruble_transactions(transaction: list) -> list:
    pass