import csv
import os

import pandas as pd

from config import PATH_HOME


def get_csv(path_name: str) -> list:
    """
    Принимает путь к csv файлу и возвращает список словарей с транзакциями.
    """

    try:
        # пробуем открыть файл
        with open(os.path.join(PATH_HOME, path_name), "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # возвращаем лист транзакций
            return list(reader)

    except Exception:
        # при возникновении ошибки, возвращаем пустой список.
        return []


def get_excel(path_name: str) -> list:
    """
    Принимает путь к Excel файлу и возвращает список словарей с транзакциями.
    """
    try:
        # пробуем прочитать Excel файл.
        excel_data = pd.read_excel(os.path.join(PATH_HOME, path_name))

        # превращаем прочитанный файл в словарь.
        data_dict = excel_data.to_dict()

        return [data_dict]

    except Exception:
        # при возникновении ошибки, возвращаем пустой список.
        return []
