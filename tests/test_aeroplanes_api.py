import pytest

from src.aeroplanes_api import AeroplanesAPI

api = AeroplanesAPI()


def test_1_coordinates_ok():
    """Тест - Получение координат"""
    coords = api.get_coordinates("Canada")
    assert len(coords) == 4
    assert coords != []


def test_coordinates_not_found():
    """Тест - Страна не найдена"""
    coords = api.get_coordinates("qqq ad")
    assert coords == []


def test_aeroplanes_ok():
    """Тест - Получение самолетов"""
    data = api.get_aeroplanes("Canada")
    assert "time" in data
    assert "states" in data


def test_aeroplanes_not_found():
    """Тест - Страна не найдена"""
    data = api.get_aeroplanes("qqq")
    assert data == {"time": 0, "states": []}
