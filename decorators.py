import functools
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> Callable:
            log_message: str = ""
            try:
                # логируем начало функции
                log_message += f"Starting {func.__name__} with inputs: {args}, {kwargs}\n"

                result: Callable = func(*args, **kwargs)

                # логируем успешное выполнение
                log_message += f"{func.__name__} ok\n"

                # записываем в файл или консоль
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end="")

                return result
            except Exception as error:
                # информация об ошибке
                error_message = f"{func.__name__} error: {type(error).__name__}. " f"Inputs: {args}, {kwargs}\n"

                # записываем в консоль
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + error_message)
                else:
                    print(log_message + error_message, end="")

                raise

        return wrapper

    return decorator
