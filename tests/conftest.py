import os
from typing import Any, Dict, Generator, List

import pytest

from src.aeroplane import Aeroplane
from src.aeroplanes_api import AeroplanesAPI
from src.json_editor import JSONEditor


@pytest.fixture
def editor() -> Generator[JSONEditor, Any, None]:
    """Фикстура: создает JSONEditor и очищает файл"""

    test_file = "data/test_aeroplanes.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    editor = JSONEditor(test_file)
    editor.save_data([])
    yield editor


@pytest.fixture
def plane1() -> Aeroplane:
    """Фикстура самолет Q1"""
    return Aeroplane("Q1", "Russia", 100, 10000.0)


@pytest.fixture
def plane2() -> Aeroplane:
    """Фикстура самолет Q1"""
    return Aeroplane("Q2", "France", 200, 11000.0)


@pytest.fixture
def plane3() -> Aeroplane:
    """Фикстура самолет Q1"""
    return Aeroplane("Q3", "United State", 200, 11000.0)


@pytest.fixture
def planes() -> Dict[str, Dict[str, Any]]:
    """Фикстура - словарь с данными тестовых самолетов"""
    return {
        "plane1": {
            "callsign": "Q1",
            "country": "Russia",
            "velocity": 100.0,
            "geo_altitude": 10000.0,
        },
        "plane2": {
            "callsign": "Q2",
            "country": "France",
            "velocity": 200.0,
            "geo_altitude": 11000.0,
        },
        "plane3": {
            "callsign": "Q3",
            "country": "United State",
            "velocity": 150.0,
            "geo_altitude": 10500.0,
        },
    }


@pytest.fixture
def aeroplanes_list(
    plane1: Aeroplane, plane2: Aeroplane, plane3: Aeroplane
) -> List[Aeroplane]:
    """Фикстура со списком трёх тестовых самолётов."""
    return [plane1, plane2, plane3]


@pytest.fixture
def data() -> Dict[str, Any]:
    return {
        "time": 1766142246,  # UNIX-время сервера OpenSky (секунды)
        "states": [
            [
                "4b1812",  # ICAO24 — уникальный идентификатор борта
                "SWR438A ",  # Callsign — позывной рейса
                "Switzerland",  # Страна регистрации ВС
                1766166618,  # time_position — время последнего обновления позиции
                1766166618,  # last_contact — время последнего контакта
                -0.0168,  # longitude — долгота (°)
                51.0888,  # latitude — широта (°)
                4267.2,  # baro_altitude — барометрическая высота (м)
                False,  # on_ground — находится ли самолёт на земле
                189.7,  # velocity — горизонтальная скорость (м/с)
                129.39,  # true_track — курс (градусы)
                14.63,  # vertical_rate — вертикальная скорость (м/с)
                None,  # sensors — ID сенсоров (null = неизвестно)
                4282.44,  # geo_altitude — геометрическая высота (м)
                "2061",  # squawk — код ответчика (транспондера)
                False,  # spi — специальный сигнал (emergency/priority)
                0,  # position_source — источник позиции
            ],
            [
                "4b1813",  # ICAO24 — уникальный идентификатор борта
                "Q1 ",  # Callsign — позывной рейса
                "Russia",  # Страна регистрации ВС
                1766166618,  # time_position — время последнего обновления позиции
                1766166618,  # last_contact — время последнего контакта
                -0.0168,  # longitude — долгота (°)
                51.0888,  # latitude — широта (°)
                4267.2,  # baro_altitude — барометрическая высота (м)
                False,  # on_ground — находится ли самолёт на земле
                189.7,  # velocity — горизонтальная скорость (м/с)
                129.39,  # true_track — курс (градусы)
                14.63,  # vertical_rate — вертикальная скорость (м/с)
                None,  # sensors — ID сенсоров (null = неизвестно)
                5282.44,  # geo_altitude — геометрическая высота (м)
                "2062",  # squawk — код ответчика (транспондера)
                False,  # spi — специальный сигнал (emergency/priority)
                0,  # position_source — источник позиции
            ],
        ],
    }
