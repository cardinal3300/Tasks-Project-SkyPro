# Виджет для банковских операций

## Обзор

Данный проект представляет собой виджет для упрощения банковских операций, разработанный на Python. Виджет предоставляет удобный интерфейс для выполнения различных задач, который на бэкенде будет готовить данные для отображения в новом виджете. Таких, как маскировка номеров банковских карт и счетов и сортировка списков словарей клиентов по датам и определённым значениям

## Установка

Для установки виджета выполните следующие шаги:

1. **Клонируйте репозиторий используя инструмент управления версиями `git`:**
    ```
    git clone <адрес вашего репозитория> cd <имя_вашего_проекта>
   ```
2. **Установите зависимости, используя менеджер пакетов `pip`:**
    ```
   pip install -r requests
   ```
## Использование

Виджет предоставляет следующие основные функции:

### 1. `get_mask_card_number(card_number)`

Функция возвращает скрытый номер карты по правилам из числа: `ХХХX XX** **** ХХХХ`, где `Х` - цифра номера карты.

*   **Параметры:**

    *   `card_number` (int или str): Номер банковской карты.

*   **Возвращаемое значение:**

    *   (str): Замаскированный номер карты.

*   **Пример:**

    python

    from your_module import get_mask_card_number # Замените your_module на имя вашего модуля

    card_number = 1234567890123456

    masked_card = get_mask_card_number(card_number)

    print(masked_card)  # Вывод: 1234 56** ** 3456

### 2. `get_mask_account(check_number)`

Функция возвращает последние 4 цифры счёта по правилам из числа: `**ХХХХ`, где `Х` - последние четыре цифры номера счета.

*   **Параметры:**

    *   `check_number` (int или str): Номер банковского номера или счета.

*   **Возвращаемое значение:**

    *   (str): Замаскированный номер или замаскированный счет.

*   **Пример:**

    python

    from your_module import get_mask_account # Замените your_module на имя вашего модуля

    account_check_number = 73654108430135874305

    masked_check_number = get_mask_account(account_check_number)

    print(masked_check_number)  # Вывод: **4305

### 3. `mask_account_card(type_and_number)`

Функция возвращает замаскированные данные типа, номера карт или счетов: `**** XX XXXX **`, где `Х` - последние четыре цифры номера счета.

*   **Параметры:**

    *   `type_and_number` (int или str): Тип с номером карты или банковским счётом.

*   **Возвращаемое значение:**

    *   (str): Замаскированный тип с номером или замаскированный счет.

*   **Пример:**

    python

    from your_module import mask_account_card # Замените your_module на имя вашего модуля

    account_type_and_number = Platinum Visa 7000792289606361

    masked_account_type_number = mask_account_card(account_type_number)

    print(masked_account_type_number)  # Вывод: 7000792289606361 7000 79** **** 6361

### 4. `get_date(data_card_number)`

Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'

*   **Параметры**

    *   `data_card_number` (str): Строка с датой.

*   **Возвращаемое значение**

    *   (str): строка с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")   

*   **Пример**

    Python

    from your_module import get_date # Замените your_module на имя вашего модуля

    account_data = 2024-03-11T02:26:18.671407

    new_account_data = get_date(account_data)

    print(new_account_data)  # Вывод: 11.03.2024

### 5. `filter_by_state(data, state="EXECUTED")`

Функция фильтрует словари по заданному значению для ключа 'state'

*   **Параметры:**

    *   `data` (List[Dict]): Список словарей.
    
    *   `state` (str, optional): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

*   **Возвращаемое значение:**

    *   (List[Dict]): Отфильтрованный список словарей.

*   **Пример:**

    python

    from your_module import filter_by_state # Замените your_module на имя вашего модуля  

    data = [{'id': 1, 'state': 'EXECUTED'},\
{'id': 2, 'state': 'PENDING'},\
{'id': 3, 'state': 'EXECUTED'}]

    executed_items = filter_by_state(data)

    print(executed_items) # Вывод: [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

### 6. `sort_by_date(data)`

Функция возвращает отсортированный список по дате

*   **Параметры**

    *   `date` (List[Dict]): Список словарей.

*   **Возвращение функции**

    *   (List[Dict]): Отсортированный список словарей по дате.
    
*   **Пример**

    python

    from your_module import sort_by_date # Замените your_module на имя вашего модуля

    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},\
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},\
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},\
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    sorted_data = sort_by_date(data)

    print(sorted_data) # [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},\
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},\
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},\
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


## Документация

Более подробную документацию по каждой функции можно найти в `docstrings` внутри исходного кода.

## Лицензия

Сведения о лицензии проекта (например, MIT, Apache 2.0) [укажите здесь](https://github.com).

## Контакты

Укажите [ваши контактные данные](https://github.com) или [способы связи](https://github.com) для обратной связи и поддержки.

