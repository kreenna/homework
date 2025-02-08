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
            log_message: str = f"Starting {func.__name__} with inputs: {args}, {kwargs}\n"
            try:
                result: Callable = func(*args, **kwargs)

                # логируем успешное выполнение
                log_message += f"{func.__name__} ok\n"

                return result
            except Exception as error:
                # информация об ошибке
                log_message += f"{func.__name__} error: {type(error).__name__}. " f"Inputs: {args}, {kwargs}\n"

                raise

            finally:
                # записываем в консоль
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end="")

        return wrapper

    return decorator
