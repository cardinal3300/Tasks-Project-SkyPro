# Виджет для банковских операций

## Обзор

Данный проект представляет собой виджет для упрощения банковских операций, разработанный на Python. Виджет предоставляет удобный интерфейс для выполнения различных задач, который на бэкенде будет готовить данные для отображения в новом виджете. Таких, как маскировка номеров банковских карт и счетов и сортировка списков словарей клиентов по датам и определённым значениям

## Установка

Для установки виджета выполните следующие шаги:

1. **Клонируйте репозиторий используя инструмент управления версиями `git`:**
    ```
    git clone github.com/cardinal3300/Tasks-Project-SkyPro cd <имя_вашего_проекта>
   ```
2. **Установите зависимости, используя менеджер пакетов `poetry`:**
    ```
   poetry install --no-root
   ```
## Использование

Виджет предоставляет следующие основные функции:

### 1. `get_mask_card_number(card_number)`

Функция возвращает замаскированный номер банковской карты, в формате XXXX XX** **** XXXX, где X - цифры.

*   **Параметры:**

    *   `card_number` (int или str): Номер банковской карты.

*   **Возвращаемое значение:**

    *   (str): Замаскированный номер карты или сообщение об ошибке (если входные данные неверны).

*   **Пример:**

    ```python
    from your_module import get_mask_card_number # Замените your_module на имя вашего модуля
    card_number = 1234567890123456
    masked_card = get_mask_card_number(card_number)
    print(masked_card)
    >>> 1234 56** ** 3456

### 2. `get_mask_account(check_number)`

Функция Маскирует номер банковского счета, отображая последние 4 цифры в формате **XXXX.

*   **Параметры:**

    *   `check_number` (int или str): Номер банковского номера или счета.

*   **Возвращаемое значение:**

    *   (str): Замаскированный номер счета или сообщение об ошибке (если входные данные неверны).

*   **Пример:**

    ```python
    from your_module import get_mask_account # Замените your_module на имя вашего модуля
    account_check_number = 73654108430135874305
    masked_check_number = get_mask_account(account_check_number)
    print(masked_check_number)
    >>> **4305

### 3. `mask_account_card(type_and_number)`

Функция маскирует номер карты или счета в зависимости от типа.

*   **Параметры:**

    *   `type_and_number` (int или str): Тип с номером карты или банковским счётом.

*   **Возвращаемое значение:**

    *   (str): Замаскированный тип с номером или замаскированный счет.

*   **Пример:**

    ```python
    from your_module import mask_account_card # Замените your_module на имя вашего модуля
    account_type_and_number = Platinum Visa 7000792289606361
    masked_account_type_number = mask_account_card(account_type_and_number)
    print(masked_account_type_number)
    >>> Visa Platinum 7000 79** **** 6361

### 4. `get_date(data_card_number)`

Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.

*   **Параметры**

    *   `data_card_number` (str): Строка с датой.

*   **Возвращаемое значение**

    *   (str): строка с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")   

*   **Пример**

    ```Python
    from your_module import get_date # Замените your_module на имя вашего модуля
    account_data = 2024-03-11T02:26:18.671407
    new_account_data = get_date(account_data)
    print(new_account_data)
    >>> 11.03.2024

### 5. `filter_by_state(data, state="EXECUTED")`

Функция фильтрует список словарей, возвращая только те, у которых значение ключа 'state' соответствует заданному.

*   **Параметры:**

    *   `data` (List[Dict]): Список словарей.
    
    *   `state` (str, optional): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

*   **Возвращаемое значение:**

    *   (List[Dict]): Отфильтрованный список словарей.

*   **Пример:**

    ```python
    from your_module import filter_by_state # Замените your_module на имя вашего модуля  
    data = [{'id': 1, 'state': 'EXECUTED'},
            {'id': 2, 'state': 'PENDING'},
            {'id': 3, 'state': 'EXECUTED'}]
    executed_items = filter_by_state(data)
    print(executed_items)
    >>> [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

### 6. `sort_by_date(data, reverse=True)`

Функция сортирует список словарей по значению ключа 'date' (в формате YYYY-MM-DD).

*   **Параметры**

    *   `date` (List[Dict]): Список словарей, каждый из которых должен содержать ключ 'date'.
    *   `reverse` (bool, optional): Флаг, указывающий порядок сортировки
(True - убывание, False - возрастание). По умолчанию
`True`.

*   **Возвращение функции**

    *   (List[Dict]): Отсортированный список словарей.
    
*   **Пример**

    ```python
    from your_module import sort_by_date # Замените your_module на имя вашего модуля
    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    sorted_data = sort_by_date(data)
    print(sorted_data)
    >>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

### 7. `filter_by_currency(transactions: List[Dict[str, Any]], currency: str)`

Функция фильтрует транзакции по заданной валюте и возвращает итератор, который последовательно выдает только те транзакции, где валюта соответствует заданному значению.

*   *Параметры:*
    *   transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
    *   currency (str): Код валюты для фильтрации, например, "USD".

*   *Возвращаемое значение:*
    *   (Iterator[Dict[str, Any]]): Итератор с отфильтрованными транзакциями.

*   *Пример:*

    ```python
    from your_module import filter_by_currency # Замените your_module на имя вашего модуля
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
    print(next(usd_transactions))
    >>> {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
        {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}
    

### 8. `transaction_descriptions(transactions: List[Dict[str, Any]])`

Функция генерирует описания транзакций из списка словарей с транзакциями.

*   *Параметры:*
    *   transactions (List[Dict[str, Any]]): Список словарей, представляющих транзакции.

*   *Возвращаемое значение:*
    *   (Iterator[str]): Итератор описаний транзакций.

*   *Пример:*

    ```python
    from your_module import transaction_descriptions # Замените your_module на имя вашего модуля
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
    print(next(descriptions))
    >>> Перевод организации
        Перевод со счета на счет
        Перевод со счета на счет
        Перевод с карты на карту
        Перевод организации
    

### 9. `card_number_generator(start: int, end: int)`

Генератор, который создает номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

*   *Параметры:*
    *   start (int): Начальное значение диапазона (включительно).
    *   end (int): Конечное значение диапазона (включительно).

*   *Возвращаемое значение:*
    *   (Iterator[str]): Итератор с номерами банковских карт в заданном диапазоне.

*   *Пример:*

    ```python
    from your_module import card_number_generator # Замените your_module на имя вашего модуля
    for card_number in card_number_generator(1, 5):
    print(card_number)
    >>> 0000 0000 0000 0001
        0000 0000 0000 0002
        0000 0000 0000 0003
        0000 0000 0000 0004
        0000 0000 0000 0005

## Тестирование

Для обеспечения надежности и качества вашего кода, были разработаны тесты с использованием pytest.

### Установка pytest и pytest-cov

1. Установите `pytest` и `pytest-cov`, выполнив команду:
    ```
   pip install pytest pytest-cov
   ```
### Запуск тестов

1. Перейдите в каталог с вашим проектом в терминале.
2. Запустите все тесты, выполнив команду:
    ```
   pytest -v --cov=your_module --cov-report=term-missing
   ```
Заменив `your_module` на имя вашего модуля Python (без расширения `.py`).
* `-v`: (verbose) - отображает подробную информацию о прохождении тестов.
* `--cov=your_module`: Указывает `pytest-cov` анализировать покрытие кода для вашего модуля.
* `--cov-report=term-missing`: Отображает строки кода, которые не были покрыты тестами.

### Анализ результатов

1. `Pytest` покажет результаты тестирования, указывая количество пройденных, пропущенных и упавших тестов.
2. `Pytest-cov` предоставит отчет о покрытии кода, показывая процент покрытия каждой функции и информацию
о строках, которые не были покрыты тестами.
3. Анализируйте результаты тестов и отчет о покрытии кода. Если какие-либо строки кода не покрыты,
рассмотрите возможность добавления новых тестов или корректировки существующих для улучшения покрытия.

## Документация

Более подробную документацию по каждой функции можно найти в `docstrings` внутри исходного кода.

## Лицензия

Сведения о лицензии проекта (например, MIT, Apache 2.0) [укажите здесь](https://github.com).

## Контакты

Укажите [ваши контактные данные](https://github.com) или
[способы связи](https://github.com) для обратной связи и поддержки.

