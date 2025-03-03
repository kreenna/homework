from src.utils import get_transactions

# Homework

Домашнее задание для Skypro

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kreenna/homework.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd homework
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   
## Тестирование

Все функции были протестированы, работают.

## Обработка файлов

Созданы функции для обработки файлов json, csv и xlsx. 

Примеры использования функций:

```python
from src.utils import get_transactions
from src.converting import get_csv, get_excel

# Пример использования get_transactions
path_json = "data/file.json"
converted_json_file = get_transactions(path_json)

# Пример использования get_csv
path_csv = "data/file.csv"
converted_csv_file = get_csv(path_csv)

# Пример использования get_excel
path_excel = "data/file.xlsx"
converted_excel_file = get_excel(path_excel)
```

## Генераторы 

Присутствуют генераторы для фильтрации транзакций по валюте, отображения описания транзакции и создания номера счета.

## Декораторы

Создан декоратор log, который логирует начало функции и ее конец, также логирует информацию о возможных ошибках.

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте pull request.