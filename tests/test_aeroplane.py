from typing import Any, Dict

import pytest

from src.aeroplane import Aeroplane

plane1 = Aeroplane("Q1", "RUSSIA", 100, 10000.0)
plane2 = Aeroplane("Q2", "RUSSIA", 200, 11000.0)
plane3 = Aeroplane("Q3", "RUSSIA", 200, 11000.0)


def test_comp_by_velocity_gt() -> None:
    """Тест - скорость меньше"""
    assert plane1 < plane2


def test_comp_by_velocity_lt() -> None:
    """Тест - скорость больше"""
    assert plane2 > plane1


def test_comp_by_velocity_eq() -> None:
    """Тест - скорость равна"""
    assert plane2 == plane3


def test_comp_by_altitude_lt() -> None:
    """Тест - высота меньше"""
    assert plane1.lower_than(plane2)


def test_comp_by_altitude_ht() -> None:
    """Тест - высота больше"""
    assert plane2.higher_than(plane1)


def test_comp_by_altitude_eq() -> None:
    """Тест - высота равна"""
    assert plane2.same_altitude(plane3)


def test_aeroplane_velocity_value_error() -> None:
    with pytest.raises(ValueError, match="Скорость не может быть отрицательной"):
        Aeroplane("Q1", "RUSSIA", -100, 10000.0)


def test_aeroplane_geo_altitude_value_error() -> None:
    with pytest.raises(ValueError, match="Высота не может быть отрицательной"):
        Aeroplane("Q1", "RUSSIA", 100, -10000.0)


def test_cast_to_object_list(data: Dict[str, Any]) -> None:
    """тест функции cast_to_object_list()"""
    result = Aeroplane.cast_to_object_list(data)

    # Проверяем количество
    assert len(result) == 2

    # Проверяем первый самолёт (SWR438A)
    assert result[0].callsign == "SWR438A"
    assert result[0].country == "Switzerland"
    assert result[0].velocity == 189.7
    assert result[0].geo_altitude == 4282.44

    # Проверяем второй самолёт (Q1)
    assert result[1].callsign == "Q1"
    assert result[1].country == "Russia"
    assert result[1].velocity == 189.7
    assert result[1].geo_altitude == 5282.44
