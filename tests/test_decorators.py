import pytest

from src.decorators import log


@log()
def successful_function(x: int, y: int) -> int:
    return x + y


@log()
def error_function(x: int, y: int) -> int:
    return x // y  # может быть ошибка деления на ноль


def test_successful_function(capsys: pytest.CaptureFixture[str]) -> None:
    result = successful_function(1, 2)
    assert result == 3

    # перехватываем данные для написания
    captured = capsys.readouterr()

    # проверяем, что были возвращены правильные данные при правильном выполнении
    assert "Starting successful_function with inputs: (1, 2), {}" in captured.out
    assert "successful_function ok" in captured.out


def test_error_function(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    # перехватываем данные с ошибкой
    captured = capsys.readouterr()

    # проверяем корректность написания данных с ошибкой
    assert "Starting error_function with inputs: (1, 0), {}" in captured.out
    assert "error_function error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_logging_to_file(tmpdir: str) -> None:
    log_file = tmpdir.join("mylog.txt")

    @log(filename=str(log_file))
    def test_func(x: int) -> int:
        return x * 2

    test_func(5)

    # читаем содержимое файла
    with open(log_file) as file:
        logs = file.read()

    assert "Starting test_func with inputs: (5,), {}" in logs
    assert "test_func ok" in logs
