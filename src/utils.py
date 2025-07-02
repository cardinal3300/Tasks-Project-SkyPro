import json
import logging

logger = logging.getLogger()
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
            else:
                logger.info("Файл не список!")
                return []
    except FileNotFoundError:
        logger.info("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.info("Файл не преобразовался в Python файл")
        return []
