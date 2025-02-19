from unittest.mock import mock_open, patch

from src.converting import get_csv, get_excel

mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')

# тестируем get_csv()


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_csv_empty_file(mock_file, mock_os_path_join):  # тест, когда файла нет
    mock_os_path_join.return_value = "fake/path/transactions.csv"

    # вызываем функцию и записываем результат в переменную
    result = get_csv("transactions.csv")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="not a csv list")
def test_csv_invalid_json_format(mock_file, mock_os_path_join):  # некорректный формат файла
    mock_os_path_join.return_value = "fake/path/transactions.csv"

    # вызываем функцию и записываем результат в переменную
    result = get_csv("transactions.csv")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", side_effect=FileNotFoundError)
def test_csv_file_not_found(mock_file, mock_os_path_join):  # файл не найден
    mock_os_path_join.return_value = "fake/path/transactions.csv"

    # вызываем функцию и записываем результат в переменную
    result = get_csv("transactions.v")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", side_effect=Exception("Some other error"))
def test_csv_other_file_error(mock_file, mock_os_path_join):  # любая другая ошибка
    mock_os_path_join.return_value = "fake/path/transactions.csv"

    # вызываем функцию и записываем результат в переменную
    result = get_csv("transactions.csv")
    assert result == []


# тестируем get_excel()


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_xlsx_empty_file(mock_file, mock_os_path_join):  # тест, когда файла нет
    mock_os_path_join.return_value = "fake/path/transactions.csv"

    # вызываем функцию и записываем результат в переменную
    result = get_excel("transactions.csv")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="not a csv list")
def test_xlsx_invalid_json_format(mock_file, mock_os_path_join):  # некорректный формат файла
    mock_os_path_join.return_value = "fake/path/transactions.xlsx"

    # вызываем функцию и записываем результат в переменную
    result = get_excel("transactions.xlsx")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", side_effect=FileNotFoundError)
def test_xlsx_file_not_found(mock_file, mock_os_path_join):  # файл не найден
    mock_os_path_join.return_value = "fake/path/transactions.xlsx"

    # вызываем функцию и записываем результат в переменную
    result = get_excel("transactions.xlsx")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", side_effect=Exception("Some other error"))
def test_xlsx_other_file_error(mock_file, mock_os_path_join):  # любая другая ошибка
    mock_os_path_join.return_value = "fake/path/transactions.xlsx"

    # вызываем функцию и записываем результат в переменную
    result = get_excel("transactions.xlsx")
    assert result == []
