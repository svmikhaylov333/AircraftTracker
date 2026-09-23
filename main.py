from src.aeroplane import Aeroplane
from src.aeroplanes_api import AeroplanesAPI
from src.json_editor import JSONEditor
from src.user_interface import (filter_aeroplanes, get_aeroplanes_by_altitude,
                                get_top_aeroplanes, print_aeroplanes,
                                sort_aeroplanes)
from src.dbmanager import DBManager


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
    pass

def user_interaction():
    print("=" * 60)
    print("Запущена программа 'Авиационный трекер AircraftTracker'")
    print("=" * 60)
    print("Выберите режим работы:")
    print("1. JSON")
    print("2. База данных (PostgreSQL)")
    print("3. Выход")
    print("=" * 60)
    choice = input ("Ваш выбор: ")
    if choice == "1":
        json_mode()
    elif choice == "2":
        db_mode()
    elif choice == "3":
        print("Bye!!!")
    else:
        print("Некорректный ввод. пока!")

if __name__ == "__main__":
    db = DBManager()
    db.create_database()
    user_interaction()
