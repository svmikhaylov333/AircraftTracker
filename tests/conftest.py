import os
from typing import Any, Dict, Generator

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
