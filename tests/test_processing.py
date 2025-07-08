from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_valid(test_data: Any) -> None:
    """Проверяет фильтрацию по состоянию."""
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "data": "2018-10-14T08:21:33.419441"},
        ],
        state="CANCELED",
    ) == [
        {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "data": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_default_state(test_data: Any) -> None:
    """Проверяет работу с параметром state по умолчанию"""
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "data": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_str(test_data: Any) -> None:
    """Проверяет значение 'state' должно быть строкой"""
    with pytest.raises(TypeError) as exc_info:
        sort_by_date(
            [
                {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": 123456, "data": 20180912212725241689},
            ]
        )
        assert exc_info.value == "Значение 'state' должно быть строкой."


def test_sort_by_date_key_data(test_data: Any) -> None:
    with pytest.raises(TypeError) as e:
        sort_by_date(
            [
                {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "": "2018-09-12T21:27:25.241689"},
            ]
        )
        assert e.value == "Отсутствует ключ 'data'."


def test_sort_by_date_valid(test_data: Any) -> None:
    """Проверяет сортировку по дате в порядке убывания."""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(test_data: Any) -> None:
    """Проверяет сортировку по дате в обратном порядке (возрастания)."""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        ],
        reverse=False,
    ) == [
        {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
    ]
