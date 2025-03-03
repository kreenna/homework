import csv
import os

import pandas as pd

from config import PATH_HOME


def get_csv(path_name: str) -> list:
    """
    Принимает путь к csv файлу и возвращает список словарей с транзакциями.
    """

    result: list = []

    try:
        with open(os.path.join(PATH_HOME, path_name), mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            # пропускаем строку с названиями
            header = next(csv_reader)

            # проходимся по каждой строке
            for values in csv_reader:
                # создаем словарь для строк
                row_dict: dict = {}

                # заполняем словарь данными
                try:
                    row_dict["id"] = int(values[0])
                    row_dict["state"] = values[1]
                    row_dict["date"] = values[2]
                    row_dict["description"] = values[8]
                    row_dict["from"] = values[6] if values[6] else None  # None, если нет данных
                    row_dict["to"] = values[7] if values[7] else None  # None, если нет данных
                    row_dict["operationAmount"] = {
                        "amount": str(values[3]),
                        "currency": {"name": values[4], "code": values[5]},
                    }
                except ValueError:
                    continue  # пропускаем строку, если возникла ошибка

                # добавляем словари в список
                result.append(row_dict)

        return result

    except Exception:
        # при возникновении ошибки, возвращаем пустой список.
        return []


def get_excel(path_name: str) -> list:
    """
    Принимает путь к Excel файлу и возвращает список словарей с транзакциями.
    """
    try:
        # пробуем прочитать файл
        df = pd.read_excel(os.path.join(PATH_HOME, path_name))

        df["id"] = df["id"].fillna(0).astype(int)

        # создаем список
        result: list = []

        # проходимся по каждой строке
        for _, row in df.iterrows():
            # заполняем словарь данными
            row_dict: dict = {
                "id": int(row["id"]),
                "state": row["state"],
                "date": row["date"].isoformat() if isinstance(row["date"], pd.Timestamp) else str(row["date"]),
                "description": row["description"],
                "from": row["from"] if pd.notna(row["from"]) else None,
                "to": row["to"] if pd.notna(row["to"]) else None,
                "operationAmount": {
                    "amount": str(row["amount"]),
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
            }

            # добавляем словари в список
            result.append(row_dict)

        return result

    except Exception:
        # при возникновении ошибки, возвращаем пустой список.
        return []
