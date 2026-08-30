from typing import Any, Dict

from requests import get

from src.base_api import BaseApi


class AeroplanesAPI(BaseApi):
    """Класс для работы с API на основе BaseAPI"""

    OPENSTREETMAP_URL = "https://nominatim.openstreetmap.org/search"
    OPENSKY_URL = "https://opensky-network.org/api/states/all?"

    def __init__(self) -> None:
        self.aeroplanes: dict[str, Any] = {}

    def get_coordinates(self, country: str) -> list:
        """Метод для получения координат выбранной страны"""
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        # Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        try:
            headers_nominatim = {
                "User-Agent": "AircraftTracker/1.0",
            }

            params_nominatim = {
                "country": country,
                "format": "json",
                "limit": 1,
            }

            response = get(
                url=self.OPENSTREETMAP_URL,
                params=params_nominatim, # type: ignore
                headers=headers_nominatim,
            )
            data_response: list = response.json()
            if not data_response:
                return []
            geo_coordinates: list[str] = data_response[0].get("boundingbox")
            if not geo_coordinates:
                return []

            return geo_coordinates
        except IndexError as exp:
            print(f"{exp}: такой страны нет")
            return []

    def get_aeroplanes(self, country: str) -> dict:
        """Метод для получения информации о самолетах в выбранной стране"""

        try:
            geo_coordinates = self.get_coordinates(country)

            # Параметры для фильтрации самолетов по их географическим координатам.
            params = {
                "lamin": geo_coordinates[0],
                "lamax": geo_coordinates[1],
                "lomin": geo_coordinates[2],
                "lomax": geo_coordinates[3],
            }

            response = get(url=self.OPENSKY_URL, params=params)

            self.aeroplanes = response.json()
            return self.aeroplanes
        except IndexError as exp:
            print(f"{exp}: такой страны нет")
            return {
                "time": 0,
                "states": [],
            }


if __name__ == "__main__":
    api = AeroplanesAPI()

    data = api.get_aeroplanes("Russia")
    print(f"Время запроса: {data['time']}\nнайдено {len(data["states"])}")
    for i, state in enumerate(data["states"]):
        print(f"{i} {state}")
