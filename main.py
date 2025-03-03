from src.converting import get_csv, get_excel
from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import get_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Основная логика программы.
    """
    transactions = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # выбор формата файла.
    while True:
        user_menu_answer: str = input(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )

        if user_menu_answer == "1":
            print("Для обработки выбран JSON-файл.")
            filename = input("Введите путь до файла: ")
            transactions.extend(get_transactions(filename))
            if transactions:
                break

            else:
                print("Неверный ввод файла. Пожалуйста, введите его в формате, например, data/file.json")
                continue

        elif user_menu_answer == "2":
            print("Для обработки выбран CSV-файл.")
            filename = input("Введите путь до файла: ")
            transactions.extend(get_csv(filename))
            if transactions:
                break

            else:
                print("Неверный ввод файла. Пожалуйста, введите его в формате, например, data/file.csv")
                continue

        elif user_menu_answer == "3":
            print("Для обработки выбран XLSX-файл.")
            filename = input("Введите путь до файла: ")
            transactions.extend(get_excel(filename))
            if transactions:
                break

            else:
                print("Неверный ввод файла. Пожалуйста, введите его в формате, например, data/file.xlsx")
                continue

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            continue

    statuses: list = ["EXECUTED", "CANCELED", "PENDING"]

    # фильтрация по статусу транзакции
    while True:
        user_state = input(
            f"""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: {', '.join(statuses)}
        """
        )

        if user_state.upper() in statuses:
            transactions = filter_by_state(transactions, user_state.upper())
            print(f'Операции отфильтрованы по статусу "{user_state.upper()}"')
            break
        else:
            print(f'Статус операции "{user_state}" недоступен. Попробуйте ещё раз.')

    # сортировка по дате
    user_sort = input(
        """Отсортировать операции по дате? Да/Нет:
        """
    ).lower()
    if user_sort == "да":
        order = input(
            """Отсортировать по возрастанию или по убыванию?:
            """
        ).lower()
        reverse: bool = True
        if order != "по убыванию":
            reverse = False
        transactions = sort_by_date(transactions, reverse)

    # фильтрация по валюте
    user_currency_filter = input(
        """Выводить только рублевые транзакции? Да/Нет:
        """
    ).lower()
    if user_currency_filter == "да":
        transactions = filter_by_currency(transactions, "RUB")

    # фильтрация по слову в описании
    user_word_filter = input(
        """Отфильтровать список транзакций по определенному слову в описании? Да/Нет:
        """
    ).lower()
    if user_word_filter == "да":
        search_word = input(
            """Введите слово для поиска:"
            """
        )
        transactions = filter_by_description(transactions, search_word)
    print(transactions)
    # вывод итогового списка транзакций
    print("Распечатываю итоговый список транзакций...")

    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")

        # форматируем транзакции
        for transaction in transactions:
            date: str = get_date(transaction["date"])
            description: str = transaction.get("description")
            card_from: str = mask_account_card(transaction.get("from"))
            card_to: str = mask_account_card(transaction.get("to"))
            transaction_sum: str = transaction["operationAmount"]["amount"]
            currency: str = transaction["operationAmount"]["currency"]["name"]

            print(f"{date}, {description}\n" f"{card_from} -> {card_to}\n" f"Сумма: {transaction_sum} {currency}\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


# --- Запуск программы ---
if __name__ == "__main__":
    main()
