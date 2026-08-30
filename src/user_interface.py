# def user_interaction():
#     country = input("Введите название страны: ")
#     top_n = int(input("Введите количество самолетов для вывода в топ N: "))
#     filter_words = input(
#         "Введите названия стран для фильтрации по стране регистрации: "
#     ).split()
#     altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
#
#     filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
#
#     ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)
#
#     sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
#     top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
#     print_aeroplanes(top_aeroplanes)



from typing import List
from src.aeroplane import Aeroplane


def filter_aeroplanes(aeroplanes: List[Aeroplane], filter_words:List) -> List[Aeroplane]:
    """функция фильтрации самолетов по списку стран регистрации"""
    filtered_aeroplanes = []

    if not filter_words:
        return aeroplanes

    for aeroplane in aeroplanes:
        for word in filter_words:
            if word.lower() == aeroplane.country.lower():
                filtered_aeroplanes.append(aeroplane)
                break
    return filtered_aeroplanes


