import json
import os

import pytest

from src.aeroplane import Aeroplane
from src.json_editor import JSONEditor


def test_add_aeroplane(editor, plane1):
    """Тест добавления самолетов"""

    editor.add_aeroplanes([plane1.to_dict()])
    data = editor.load_data()
    assert len(data) == 1
    assert data[0]["callsign"] == "Q1"


def test_add_aeroplanes(editor, planes):
    """Тест добавления самолетов"""

    editor.add_aeroplanes(list(planes.values()))
    data = editor.load_data()
    assert len(data) == 3
    assert data[0]["callsign"] == "Q1"
    assert data[1]["callsign"] == "Q2"
    assert data[2]["callsign"] == "Q3"


def test_get_aeroplanes(editor, planes):
    """Тест - получение информации всех самолетов"""
    editor.add_aeroplanes(list(planes.values()))
    data = editor.get_aeroplanes()
    assert len(data) == 3


def test_get_aeroplanes_filter_callsign(editor, planes):
    """Тест - получение информации самолетов (фильтрация по позывному"""
    editor.add_aeroplanes(list(planes.values()))
    data = editor.get_aeroplanes(callsign="Q1")
    assert len(data) == 1
    assert data[0]["callsign"] == "Q1"


def test_delete_aeroplanes_by_callsign(editor, planes):
    """Тест - удаления по позывному"""
    editor.add_aeroplanes(list(planes.values()))

    editor.delete_aeroplanes("Q1")
    data = editor.load_data()
    assert len(data) == 2
    assert data[0]["callsign"] == "Q2"
    assert data[1]["callsign"] == "Q3"


def test_delete_aeroplanes_empty_criteria(editor, planes):
    """Тест - удаление без критериев - ничего не удалится"""
    editor.add_aeroplanes(list(planes.values()))

    editor.delete_aeroplanes()
    data = editor.load_data()
    assert len(data) == 3


def test_delete_aeroplanes_two_criteria(editor, planes):
    """Тест - удаление по нескольким критериям"""
    editor.add_aeroplanes(list(planes.values()))

    editor.delete_aeroplanes(country="France", velocity=150)
    data = editor.load_data()

    assert len(data) == 1
    assert data[0]["callsign"] == "Q1"


def test_save_data(editor, plane1):
    """Тест - сохранения данных"""
    data = [plane1.to_dict()]
    editor.save_data(data)

    loaded = editor.load_data()
    assert len(loaded) == 1
    assert loaded[0]["callsign"] == "Q1"
