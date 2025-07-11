import json
import re
import logging
from collections import Counter

#Объект логера:


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Запуск функции `reading_json_file`")
    try:
        with open(file_path, encoding="utf-8") as file:
            logger.info("Открываем файл...")
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл получен, всё ок")
            return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Файл не преобразовался в Python файл")
        return []


def process_bank_search(operations:list[dict], search:str) -> list[dict]:
    """Функция, возвращающая список словарей, у которых в описании есть строка от пользователя."""
    result: list[dict] = []
    re_pattern = re.compile(search, re.IGNORECASE)
    for operation in operations:
        if re_pattern.search(str(operation.get("description", ""))):
            result.append(operation)
    return result


def process_bank_counter(data: list[dict], categories: list) -> dict:
    """Функция, возвращающая словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    descriptions = [operation.get("description") for operation in data]
    categories_counter = Counter(descriptions)
    category_count = {category: categories_counter[category] for category in categories}
    return category_count
