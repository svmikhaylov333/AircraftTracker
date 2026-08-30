from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseFileEditor(ABC):
    """абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_aeroplanes(self, aeroplane_data: List[Dict[str, Any]]) -> None:
        """Добавление информации о самолетах в файл"""
        pass

    @abstractmethod
    def get_aeroplanes(self, *args, **kwargs) -> List[Dict[str, Any]]:
        """ "Получение информации о самолетах из файла по заданному критерию"""
        pass

    @abstractmethod
    def delete_aeroplanes(self, *args, **kwargs) -> None:
        """ "Удаление информации о самолетах по заданному критерию"""
        pass

    @abstractmethod
    def load_data(self) -> List[Dict[str, Any]]:
        """Загрузка данных из файла"""
        pass

    @abstractmethod
    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохранение данных в файл"""
        pass
