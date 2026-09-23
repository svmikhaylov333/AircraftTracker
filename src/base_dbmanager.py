from abc import ABC, abstractmethod
from typing import List, Optional


class BaseDBManager (ABC):
    """Абстрактный класс для работы с БД"""

    @abstractmethod
    def get_countries_and_aeroplanes_count(self) -> List:
        """получает список всех стран и количество самолетов в их воздушных пространствах"""
        pass

    @abstractmethod
    def get_all_aeroplanes(self) -> List:
        """получает список всех воздушных судов"""
        pass

    @abstractmethod
    def get_avg_speed(self) -> Optional[float]:
        """получает среднюю скорость по самолетам"""
        pass

    @abstractmethod
    def get_aeroplanes_with_higher_speed(self) -> List:
        """получает список всех самолетов, у которых скорость выше средней"""
        pass

    @abstractmethod
    def get_aeroplanes_with_keyword(self, symbols: str) -> List:
        """получает список всех самолетов, в позывном которых содержатся переданные в метод символы."""
        pass


