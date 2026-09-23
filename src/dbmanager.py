from typing import List, Optional

import psycopg2

from src.base_dbmanager import BaseDBManager
from src.config import config

class DBManager(BaseDBManager):
    """Класс для работы с БД PostgreSQL"""
    def __init__(self, config_path: str = 'database.ini') -> None:
        # Загрузка данных из ini файла
        self.params = config(config_path)

        ## Подключение к базе данных
        # ** распаковывает словарь в именованные арг-ты dbname="aircraft_tracker" и т.д.
        self.conn = psycopg2.connect(**self.params)
        # чтобы не писать conn.commit()/ после команды сразу добавление в БД
        self.conn.autocommit = True
        # Открытие курсора
        self.cur = self.conn.cursor()


    def __del__(self) -> None:
        for attr in ("cur", "conn"):
            obj = getattr(self, attr, None)
            if obj is not None:
                try:
                    obj.close()
                except Exception as exp:
                    print(f"Ошибка при закрытии {attr}: {exp}")


    def get_countries_and_aeroplanes_count(self) -> List:
        """получает список всех стран и количество самолетов в их воздушных пространствах"""
        pass


    def get_all_aeroplanes(self) -> List:
        """получает список всех воздушных судов"""
        pass


    def get_avg_speed(self) -> Optional[float]:
        """получает среднюю скорость по самолетам"""
        pass

    def get_aeroplanes_with_higher_speed(self) -> List:
        """получает список всех самолетов, у которых скорость выше средней"""
        pass


    def get_aeroplanes_with_keyword(self, symbols:str) -> List:
        """получает список всех самолетов, в позывном которых содержатся переданные в метод символы."""
        pass