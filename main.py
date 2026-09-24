from src.aeroplane import Aeroplane
from src.aeroplanes_api import AeroplanesAPI
from src.dbmanager import DBManager
from src.json_editor import JSONEditor
from src.user_interface import (filter_aeroplanes, get_aeroplanes_by_altitude,
                                get_top_aeroplanes, print_aeroplanes,
                                sort_aeroplanes)

# # Создание экземпляра класса для работы с API сайтов с самолетами
# api = AeroplanesAPI()
#
# # Получение информации о самолетах с opensky-network.org
# aeroplanes = api.get_aeroplanes("Spain")
#
# # Преобразование набора данных в список объектов
# aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
#
# # Пример работы конструктора класса с одним самолетом
# aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
#
# # Сохранение информации в файл
# json_saver = JSONEditor()
# json_saver.add_aeroplanes([aeroplane.to_dict()])
# # удаление добавленного самолета
# json_saver.delete_aeroplanes("UAL1621")


# Функция для взаимодействия с пользователем (JSON)
def json_mode():

    country = input("Введите название страны (на Английском): ")
    print(f"получение данных над {country}...")
    api = AeroplanesAPI()
    data = api.get_aeroplanes(country)
    aeroplanes = Aeroplane.cast_to_object_list(data)
    print(f"Найдено {len(aeroplanes)} самолетов")

    editor = JSONEditor()
    aeroplanes_data = [aeroplane.to_dict() for aeroplane in aeroplanes]
    editor.save_data(aeroplanes_data)
    print(f"Сохранено {len(aeroplanes_data)} самолетов")

    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input(
        "Введите названия стран для фильтрации по стране регистрации: "
    ).split()
    altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    # print(filtered_aeroplanes)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)


# Функция для взаимодействия с пользователем (PostgreSQL)
def db_mode():
    """Режим работы с PostgreSQL."""
    print("\n" + "=" * 60)
    print("Режим работы с База данных (PostgreSQL)")
    database = DBManager()
    database.create_database()  # пересоздаст БД!!!
    print("\n" + "=" * 60)
    print("Загрузка самолётов из API в БД")
    print("=" * 60)
    print("Использовать страны по умолчанию?")
    print(
        "\n"
        '        По умолчанию: ["Turkey", "Sweden", "Spain", "Iceland", "Russia", \n'
        '        "United Kingdom", "United States", "France", "Switzerland", "Kingdom of the Netherlands"]'
    )
    print("1. Да")
    print("2. Нет")
    print("=" * 60)

    choice = input("Ваш выбор: ").strip()
    countries = []

    if choice == "1":
        countries = [
            "Turkey",
            "Sweden",
            "Spain",
            "Iceland",
            "Russia",
            "United Kingdom",
            "United States",
            "France",
            "Switzerland",
            "Kingdom of the Netherlands",
        ]
    elif choice == "2":
        countries_input = input("Введите 10 стран через запятую на английском: ")
        countries = [c.strip() for c in countries_input.split(",")]

        if len(countries) != 10:
            print(
                f"Нужно ровно 10 стран, введено {len(countries)}. Используем по умолчанию."
            )
            countries = [
                "Turkey",
                "Sweden",
                "Spain",
                "Iceland",
                "Russia",
                "United Kingdom",
                "United States",
                "France",
                "Switzerland",
                "Kingdom of the Netherlands",
            ]

    # Загрузка данных
    api = AeroplanesAPI()
    total_loaded = 0

    for country in countries:
        print(f"\nЗагрузка: {country}...")
        try:
            data = api.get_aeroplanes(country)
            aeroplanes = Aeroplane.cast_to_object_list(data)

            if aeroplanes:
                database.insert_aeroplanes(aeroplanes, country)
                total_loaded += len(aeroplanes)
                print(f"{country}: {len(aeroplanes)} самолётов")
            else:
                print(f"{country}: самолёты не найдены")
        except Exception as exp:
            print(f"{country}: ошибка — {exp}")

    print("\n" + "=" * 60)
    print(f"Всего загружено: {total_loaded} самолётов")
    print("=" * 60)

    # Меню работы с БД
    while True:
        print("\n" + "=" * 60)
        print("Режим работы с БД (PostgreSQL)")
        print("=" * 60)
        print("0. Выход")
        print("1. Показать все самолёты")
        print("2. Показать страны и количество самолётов")
        print("3. Показать среднюю скорость")
        print("4. Показать самолёты быстрее средней")
        print("5. Поиск по позывному")
        print("=" * 60)

        choice = input("Ваш выбор: ")

        if choice == "1":
            rows = database.get_all_aeroplanes()
            print(f"\nВсего самолётов: {len(rows)}")
            for row in rows:
                print(row)
        elif choice == "2":
            rows = database.get_countries_and_aeroplanes_count()
            print(f"\nСтран: {len(rows)}")
            for row in rows:
                print(f"{row[0]}: {row[1]} самолётов")
        elif choice == "3":
            avg = database.get_avg_speed()
            print(f"\nСредняя скорость: {avg} м/с")
        elif choice == "4":
            rows = database.get_aeroplanes_with_higher_speed()
            print(f"\nСамолётов быстрее средней: {len(rows)}")
            for row in rows:
                print(row)
        elif choice == "5":
            keyword = input("Введите часть позывного: ").strip()
            if keyword:
                rows = database.get_aeroplanes_with_keyword(keyword)
                print(f"\nНайдено: {len(rows)}")
                for row in rows:
                    print(row)
            else:
                print("Пустой ввод")
        elif choice == "0":
            print("Bye!!!")
            break
        else:
            print("Некорректный ввод")


def user_interaction():
    print("=" * 60)
    print("Запущена программа 'Авиационный трекер AircraftTracker'")
    print("=" * 60)
    print("Выберите режим работы:")
    print("1. JSON")
    print("2. База данных (PostgreSQL)")
    print("3. Выход")
    print("=" * 60)
    choice = input("Ваш выбор: ")
    if choice == "1":
        json_mode()
    elif choice == "2":
        db_mode()
    elif choice == "3":
        print("Bye!!!")
    else:
        print("Некорректный ввод. пока!")


if __name__ == "__main__":

    user_interaction()
