import functools
from typing import Any, Callable


def log(filename: str) -> Callable:
    """Декоратор для логирования вызова функции"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                with open(filename, "a", encoding="UTF-8") as file:
                    file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                with open(filename, "a", encoding="UTF-8") as file:
                    file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
