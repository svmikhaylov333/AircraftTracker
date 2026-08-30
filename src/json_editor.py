import json
import os
from typing import Any, Dict, List

from src.base_file_editor import BaseFileEditor


class JSONEditor(BaseFileEditor):
    """Класс для работы с JSON-файлом"""

    def __init__(self, file_path: str = "data/aeroplanes.json"):
        self.file_path = file_path
        self.make_dir()

    def make_dir(self):
        dir_path = os.path.dirname(self.file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def _save_json(self, data: List[Dict[str, Any]]) -> None:
        self.make_dir()
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self) -> List[Dict[str, Any]]:
        """Загрузка данных из файла"""
        return self._load_json()

    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохранение данных в файл"""
        self._save_json(data)

    def _load_json(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_aeroplanes(self, aeroplane_data: List[Dict[str, Any]]) -> None:
        """добавление информации о самолтах в файл"""

        data = self._load_json()

        for new_aeroplane in aeroplane_data:
            callsign = new_aeroplane.get("callsign")
            for i, aeroplane_item in enumerate(data):
                if aeroplane_item.get("callsign") == callsign:
                    data[i] = new_aeroplane
                    break
            else:
                data.append(new_aeroplane)

        self._save_json(data)

    def get_aeroplanes(self, *args, **kwargs) -> List[Dict[str, Any]]:
        """Получение информации по критерию"""

        data = self._load_json()

        if kwargs:
            result = []
            for aeroplane in data:

                if all(aeroplane.get(key) == value for key, value in kwargs.items()):
                    result.append(aeroplane)
            data = result

        if args:
            callsigns = args
            result = []
            for aeroplane in data:
                if aeroplane.get("callsign") in callsigns:
                    result.append(aeroplane)
            data = result

        return data

    def delete_aeroplanes(self, *args, **kwargs) -> None:
        """Удаление информации о самолетах по заданному критерию"""
        data = self._load_json()

        if args:
            callsigns = args
            data = [
                aeroplane
                for aeroplane in data
                if aeroplane.get("callsign") not in callsigns
            ]
        if kwargs:
            result = []
            for aeroplane in data:
                for key, value in kwargs.items():
                    if aeroplane.get(key) == value:
                        break
                else:
                    result.append(aeroplane)
            data = result

        self._save_json(data)
