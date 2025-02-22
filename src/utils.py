import json
import logging
import os

from config import PATH_HOME

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename=os.path.join(PATH_HOME, "logs/utils.log"),  # запись логов в файл
    filemode="w",
    encoding="utf-8",
)  # перезапись файла при каждом запуске


def get_transactions(path_name: str) -> list:
    """
    Принимает путь до JSON-файла и возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """

    logging.info("Пробуем открыть файл по указанному пути.")
    try:
        with open(os.path.join(PATH_HOME, path_name), "r", encoding="utf-8") as file:
            converted_data: list = json.load(file)

        logging.info("Проверяем корректность формата файла.")
        if not isinstance(converted_data, list):  # проверяем, что файл в нужном формате
            return []

    except Exception as error:  # любые ошибки с файлом

        logging.error(f"Произошла ошибка при обработке файла: {error}.")
        return []

    logging.info("Файл прошел проверку.")
    return converted_data
