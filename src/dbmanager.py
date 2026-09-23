from typing import List, Optional

import psycopg2

from src.base_dbmanager import BaseDBManager
from src.config import config

class DBManager(BaseDBManager):
    """Класс для работы с БД PostgreSQL"""
    def __init__(self, config_path: str = 'database.ini') -> None:
        """Подключение к БД PostgreSQL с данными из ini-файла"""
        # Загрузка данных из ini файла
        self.params = config(config_path)
        self.conn = None
        self.cur = None

        # self.params = config(config_path)
        #
        # ## Подключение к базе данных
        # # ** распаковывает словарь в именованные арг-ты dbname="aircraft_tracker" и т.д.
        # self.conn = psycopg2.connect(**self.params)
        # # чтобы не писать conn.commit()/ после команды сразу добавление в БД
        # self.conn.autocommit = True
        # # Открытие курсора
        # self.cur = self.conn.cursor()
        #
        # self.create_database()


    def __del__(self) -> None:
        for attr in ("cur", "conn"):
            """Закрытие курсора и соединения"""
            obj = getattr(self, attr, None)
            if obj is not None:
                try:
                    obj.close()
                except Exception as exp:
                    print(f"Ошибка при закрытии {attr}: {exp}")

    def create_database(self) -> None:
        """Создание базы данных и таблиц """

        database_name = self.params["dbname"]


        # Организуем подключение к системной БД
        params = {**self.params, "dbname": "postgres"}
        conn = psycopg2.connect(**params)
        conn.autocommit = True

        # ????узнать как отключить всех пользователей от целевой БД

        # Удаляем и создаем БД из ini
        cur = conn.cursor()
        try:
            cur.execute(f"DROP DATABASE IF EXISTS {self.params['dbname']}")
            cur.execute(f"CREATE DATABASE {self.params['dbname']}")
            print(f"Новая БД {database_name} создана")
        except Exception as exp:
            print(f"Ошибка {exp}")
        finally:
            cur.close()
            conn.close()
        #Переподключаемся к новосозданной базе
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

        # Создание таблиц countries и aeroplanes."""
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS countries (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS aeroplanes (
                    id SERIAL PRIMARY KEY,
                    icao24 VARCHAR(10) UNIQUE NOT NULL,
                    callsign VARCHAR(20),
                    origin_country VARCHAR(100),
                    latitude FLOAT,
                    longitude FLOAT,
                    altitude FLOAT,
                    velocity FLOAT
                )
            """)
        print("Таблицы созданы")

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