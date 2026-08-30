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
