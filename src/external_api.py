import os

import requests
from dotenv import load_dotenv


def get_ruble_transactions(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """
    if transaction and isinstance(transaction, dict):  # проверяем корректность данных

        currency: str = transaction["operationAmount"]["currency"]["code"]
        amount: float = transaction["operationAmount"]["amount"]

        if currency == "RUB":
            return amount

        else:
            try:
                url: str = "https://api.apilayer.com/exchangerates_data/convert"
                payload: dict = {"to": "RUB", "from": currency, "amount": amount}  # задаем параметры

                load_dotenv()
                API_KEY = os.getenv("API_KEY")  # получаем API-ключ
                headers: dict = {"apikey": API_KEY}

                response = requests.get(url, headers=headers, params=payload)  # получаем ответ

                return response.json()["result"]

            except Exception:
                return 0
    else:
        return 0
