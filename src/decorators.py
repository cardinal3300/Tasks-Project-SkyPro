from typing import Any, Callable, Optional


def message_log(message: str, filename: Optional[str] = None) -> None:
    """Функция для логирования записи в файл."""
    if filename:
        with open(filename, "a", encoding="UTF-8") as file:
            file.write(message)
    else:
        print(message)


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызова функции."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} - ok - {result}\n"
                message_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__}: - {type(e)} - args: {args} - kwargs: {kwargs}\n"
                message_log(message, filename)
                raise

        return wrapper

    return decorator


@log(filename="log.txt")
def my_func(x: int, y: int) -> int:
    return x + y


my_func(2, 3)
