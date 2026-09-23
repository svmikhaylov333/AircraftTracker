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

        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()


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

        # Отключить всех пользователей
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT pg_terminate_backend(pid)
                        FROM pg_stat_activity
                        WHERE datname = '{database_name}' AND pid <> pg_backend_pid()
                    """)
        # Удаляем и создаем БД из ini (Может лучше не удалять??? Подумать)
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
                    callsign VARCHAR(50) NOT NULL,
                    country_id INTEGER REFERENCES countries(id) ON DELETE CASCADE,
                    velocity FLOAT NOT NULL,
                    geo_altitude FLOAT NOT NULL,
                    UNIQUE(callsign)
                )
            """)
        print("Таблицы созданы")

    def get_countries_and_aeroplanes_count(self) -> List:
        """получает список всех стран и количество самолетов в их воздушных пространствах"""
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, COUNT(a.id) AS aeroplanes_count
                FROM countries c
                JOIN aeroplanes a ON a.country_id = c.id
                GROUP BY c.name
                ORDER BY aeroplanes_count DESC;
            """)
            return cur.fetchall()



    def get_all_aeroplanes(self) -> List:
        """получает список всех воздушных судов"""
        with self.conn.cursor() as cur:
            cur.execute("""
                       SELECT a.callsign, c.name, a.velocity, a.geo_altitude
                       FROM aeroplanes a
                       JOIN countries c ON a.country_id = c.id
                       ORDER BY a.callsign;
                   """)
            return cur.fetchall()


    def get_avg_speed(self) -> Optional[float]:
        """получает среднюю скорость по самолетам"""
        with self.conn.cursor() as cur:
            cur.execute("SELECT AVG(velocity) FROM aeroplanes;")
            result = cur.fetchone()
            return result[0] if result else None

    def get_aeroplanes_with_higher_speed(self) -> List:
        """получает список всех самолетов, у которых скорость выше средней"""
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT a.callsign, c.name, a.velocity, a.geo_altitude
                FROM aeroplanes a
                JOIN countries c ON a.country_id = c.id
                WHERE a.velocity > (SELECT AVG(velocity) FROM aeroplanes)
                ORDER BY a.velocity DESC;
            """)
            return cur.fetchall()


    def get_aeroplanes_with_keyword(self, symbols:str) -> List:
        """получает список всех самолетов, в позывном которых содержатся переданные в метод символы."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT a.callsign, c.name, a.velocity, a.geo_altitude
                FROM aeroplanes a
                JOIN countries c ON a.country_id = c.id
                WHERE a.callsign ILIKE %s
                ORDER BY a.callsign;
                """,
                (f"%{symbols}%",),
            )
            return cur.fetchall()