from typing import List

from src.aeroplane import Aeroplane


def filter_aeroplanes(
    aeroplanes: List[Aeroplane], filter_words: List
) -> List[Aeroplane]:
    """Функция фильтрации самолетов по списку стран регистрации"""
    filtered_aeroplanes = []

    if not filter_words:
        return aeroplanes

    for aeroplane in aeroplanes:
        for word in filter_words:
            if word.lower().strip() in aeroplane.country.lower().strip():
                filtered_aeroplanes.append(aeroplane)
                break
    return filtered_aeroplanes


def get_aeroplanes_by_altitude(
    aeroplanes: List[Aeroplane], altitude_range: str
) -> List[Aeroplane]:
    """Функция фильтрации самолетов по высоте"""
    try:
        filtered_aeroplanes = []

        range_morph = altitude_range.replace("-", " ").split()
        if len(range_morph) == 2:
            min_altitude, max_altitude = float(range_morph[0]), float(range_morph[1])
        elif len(range_morph) == 1:
            min_altitude, max_altitude = float(range_morph[0]), float("inf")
        else:
            return aeroplanes

        for aeroplane in aeroplanes:
            if min_altitude <= aeroplane.geo_altitude <= max_altitude:
                filtered_aeroplanes.append(aeroplane)
        return filtered_aeroplanes
    except ValueError:
        print("Некорректный формат диапазона. Используйте: '10000 - 15000'")
        return aeroplanes




def sort_aeroplanes(aeroplanes: List[Aeroplane]) -> List[Aeroplane]:
    """Сортировка самолетов по высоте (по убыванию)"""
    return sorted(aeroplanes, key=lambda p: p.geo_altitude, reverse=True)


def get_top_aeroplanes(aeroplanes: List[Aeroplane], top_n: int) -> List[Aeroplane]:
    """Получение топ N самолетов"""
    if top_n <= 0:
        return []
    return aeroplanes[:top_n]


def print_aeroplanes(aeroplanes: List[Aeroplane]) -> None:
    """Вывод самолетов в консоль"""
    if not aeroplanes:
        print("Самолеты не найдены")
        return

    print(f"\nНайдено: {len(aeroplanes)} самолетов")
    print("=" * 30)
    for i, aeroplane in enumerate(aeroplanes, 1):
        print(
            f"{i}. {aeroplane.callsign}, {aeroplane.country}, "
            f"скорость: {aeroplane.velocity} м/с, высота: {aeroplane.geo_altitude} м"
        )
    print("=" * 30)
