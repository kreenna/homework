from unittest.mock import patch

import pytest

from main import main


@pytest.fixture
def mock_transactions():
    """
    Фикстура для моков.
    """
    return [
        {
            "date": "2025-02-20T00:00:00Z",
            "description": "Test transaction",
            "from": "1234567890123456",
            "to": "6543210987654321",
            "operationAmount": {"amount": "1000", "currency": {"name": "RUB"}},
            "state": "EXECUTED",
        }
    ]


@patch("main.get_transactions")
@patch("main.filter_by_state")
@patch("main.sort_by_date")
@patch("main.filter_by_currency")
@patch("main.filter_by_description")
@patch("main.get_date")
@patch("main.mask_account_card")
@patch("builtins.print")
def test_main_function(
    mock_print,
    mock_mask_account_card,
    mock_get_date,
    mock_filter_by_description,
    mock_filter_by_currency,
    mock_sort_by_date,
    mock_filter_by_state,
    mock_get_transactions,
    mock_transactions,
    monkeypatch,
):

    inputs = iter(
        [
            "1",
            "path/to/file.json",
            "EXECUTED",
            "да",
            "по убыванию",
            "да",
            "да",
            "test",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    mock_get_transactions.return_value = mock_transactions
    mock_filter_by_state.return_value = mock_transactions
    mock_sort_by_date.return_value = mock_transactions
    mock_filter_by_currency.return_value = mock_transactions
    mock_filter_by_description.return_value = mock_transactions
    mock_get_date.return_value = "2025-02-20"
    mock_mask_account_card.side_effect = lambda x: f"****{x[-4:]}"

    main()

    mock_get_transactions.assert_called_once_with("path/to/file.json")
    mock_filter_by_state.assert_called_once_with(mock_transactions, "EXECUTED")
    mock_sort_by_date.assert_called_once_with(mock_transactions, True)
    mock_filter_by_currency.assert_called_once_with(mock_transactions, "RUB")
    mock_filter_by_description.assert_called_once_with(mock_transactions, "test")

    mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
    mock_print.assert_any_call("Всего банковских операций в выборке: 1")

    expected_output = "2025-02-20, Test transaction\n" "****3456 -> ****4321\n" "Сумма: 1000 RUB\n"
    mock_print.assert_any_call(expected_output)
