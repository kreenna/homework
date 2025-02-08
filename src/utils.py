import json
import os


def get_transactions(path: str) -> list:
    with open(path, 'r') as file:
        converted_data = json.load(file)

    return list(converted_data)

print(get_transactions(r"data\data.json"))