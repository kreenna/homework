from unittest.mock import mock_open, patch

from src.utils import get_transactions

mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')


@patch("builtins.open", mocked_open)
def test_get_transactions(mock_file) -> None:
    result: list = get_transactions("data/operations.json")
    assert result == [{"id": 1, "amount": "100.0"}]
    mock_file.assert_called_once_with("data/operations.json", "r")
