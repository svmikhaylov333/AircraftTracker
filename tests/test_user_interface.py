from typing import List

import pytest

from src.aeroplane import Aeroplane
from src.user_interface import (filter_aeroplanes, get_aeroplanes_by_altitude,
                                get_top_aeroplanes, print_aeroplanes,
                                sort_aeroplanes)


def test_filter_aeroplanes_one_country(aeroplanes_list: list[Aeroplane]) -> None:
    """Фильтрация по одной стране"""
    result = filter_aeroplanes(aeroplanes_list, ["Russia"])
    assert len(result) == 1
    assert result[0].country == "Russia"


def test_filter_aeroplanes_mult_countries(aeroplanes_list: list[Aeroplane]) -> None:
    """Фильтрация по нескольким странам"""

    result = filter_aeroplanes(aeroplanes_list, ["Russia", "France"])
    assert len(result) == 2
    countries = {p.country for p in result}
    assert "Russia" in countries
    assert "France" in countries


def test_filter_aeroplanes_no_match(aeroplanes_list: list[Aeroplane]) -> None:
    """Страна не найдена -> пустой список"""

    result = filter_aeroplanes(aeroplanes_list, ["wqwefewf"])
    assert len(result) == 0


def test_get_aeroplanes_by_altitude_range(aeroplanes_list: List[Aeroplane]) -> None:
    """Фильтрация по диапазону высот"""
    result = get_aeroplanes_by_altitude(aeroplanes_list, "10000 - 11000")
    assert len(result) == 3


def test_get_aeroplanes_by_min_altitude(aeroplanes_list: List[Aeroplane]) -> None:
    """Фильтрация с указанием только нижней границы"""
    result = get_aeroplanes_by_altitude(aeroplanes_list, "10500")
    assert len(result) == 2
    for p in result:
        assert p.geo_altitude >= 10500


def test_get_aeroplanes_by_no_altitude(aeroplanes_list: List[Aeroplane]) -> None:
    """Нет самолётов в указанном диапазоне/ возвращает пустой список"""
    result = get_aeroplanes_by_altitude(aeroplanes_list, "50000 - 60000")
    assert len(result) == 0


def test_sort_aeroplanes(aeroplanes_list: List[Aeroplane]) -> None:
    """Сортировка по высоте (по убыванию)"""
    result = sort_aeroplanes(aeroplanes_list)
    assert result[0].geo_altitude == 11000.0
    assert result[1].geo_altitude == 11000.0
    assert result[2].geo_altitude == 10000.0


def test_get_top_aeroplanes(aeroplanes_list: List[Aeroplane]) -> None:
    """Получение топ самолётов"""
    result = get_top_aeroplanes(aeroplanes_list, 2)
    assert len(result) == 2
    assert result[0] == aeroplanes_list[0]
    assert result[1] == aeroplanes_list[1]


def test_print_aeroplanes(capsys, aeroplanes_list: List[Aeroplane]) -> None:
    """Проверка вывода в консоль"""
    print_aeroplanes(aeroplanes_list)
    captured = capsys.readouterr()
    assert "Найдено: 3 самолетов" in captured.out
    assert "Q1" in captured.out
    assert "Q2" in captured.out


def test_print_aeroplanes_empty(capsys) -> None:
    """Вывод при пустом списке"""
    print_aeroplanes([])
    captured = capsys.readouterr()
    assert "Самолеты не найдены" in captured.out
