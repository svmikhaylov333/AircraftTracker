from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Базовый Класс должен уметь подключаться к API и получать географические координаты стран
    и информацию о самолетах, находящихся в воздушном пространстве этих стран."""

    @abstractmethod
    def get_coordinates(self, country: str) -> list:
        """метод получения координат выбранной страны"""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> dict:
        """метод для получения списка всех самолетов над выбранной странной"""
        pass
