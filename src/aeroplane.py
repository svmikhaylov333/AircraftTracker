
# aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
from src.aeroplanes_api import AeroplanesAPI

class Aeroplane:
    """Класс для работы с информацией о самолетах"""

    def __init__(self, callsign:str, country:str, velocity: float, geo_altitude: float, ):

        self.callsign = callsign        # Callsign — позывной рейса
        self.country = country          # Страна регистрации ВС

        if velocity >= 0:
            self.velocity = velocity    # velocity — горизонтальная скорость (м/с)
        else:
            print(f"velocity={velocity} < 0, выбрасываем ValueError")
            raise ValueError("Скорость не может быть отрицательной")

        if geo_altitude >= 0:          # geo_altitude — геометрическая высота (м)
            self.geo_altitude = geo_altitude
        else:
            print(f"geo_altitude={geo_altitude} < 0, выбрасываем ValueError")
            raise ValueError("Высота не может быть отрицательной")

    def __eq__(self, other) -> bool:
        """Метод сравнения скорости - равно"""
        if type(other) is type(self):
            return self.velocity == other.velocity
        raise TypeError("Можно сравнивать только одинаковые типы")

    def __gt__(self, other) -> bool:
        """Метод сравнения скорости - больше"""
        if type(other) is type(self):
            return self.velocity > other.velocity
        raise TypeError("Можно сравнивать только одинаковые типы")

    def __lt__(self, other) -> bool:
        """Метод сравнения скорости - меньше"""
        if type(other) is type(self):
            return self.velocity < other.velocity
        raise TypeError("Можно сравнивать только одинаковые типы")

    def higher_than(self, other: 'Aeroplane') -> bool:
        """Метод сравнения высоты - больше"""
        if type(other) is type(self):
            return self.geo_altitude > other.geo_altitude
        raise TypeError("Можно сравнивать только одинаковые типы")


    def lower_than(self, other: 'Aeroplane') -> bool:
        """Метод сравнения высоты - меньше"""
        if type(other) is type(self):
            return self.geo_altitude < other.geo_altitude
        raise TypeError("Можно сравнивать только одинаковые типы")

    def same_altitude(self, other: 'Aeroplane') -> bool:
        """Метод сравнения высоты - равно"""
        if type(other) is type(self):
            return self.geo_altitude == other.geo_altitude
        raise TypeError("Можно сравнивать только одинаковые типы")




