import logging

import requests

from config.settings import OPEN_WEATHER_API_KEY

logger = logging.getLogger(__name__)


class WeatherApi:
    """
    Get weather from API and parse the data
    """

    def __init__(self, city: str):
        self.weather_data = self.get_weather(city)

    def get_temp_feels_like(self) -> int:
        return self.weather_data["main"]["feels_like"]

    @staticmethod
    def get_weather(city: str) -> dict:
        """
        Make API call for weather for the neaarest city.
        Return the first weather group digit.
        """
        weather_data = {}
        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather",
                params={
                    "appid": OPEN_WEATHER_API_KEY,
                    "q": city,
                    "units": "metric"
                }
            )
            r.raise_for_status()
            weather_data = r.json()
        except Exception as e:
            logger.exception(f"Problem getting weather group: {e}")
        return weather_data

    def get_weather_colour(self) -> str:
        """
        Decide colour based on weather conditions and temperature retrieved from API.
        """
        weather_colour = ""
        try:
            group_id = self.weather_data["weather"][0]["id"]
            temp_feels_like = self.get_temp_feels_like()
            if group_id < 600:  # Wet
                weather_colour = "blue"
            elif group_id == 800:  # Clear
                weather_colour = self.colour_from_temperature(temp_feels_like)
            else:  # Cloudy/Atmosphere
                weather_colour = self.colour_from_temperature(temp_feels_like)
        except Exception as e:
            logger.exception(f"Problem parsing weather: {e}")
        return weather_colour

    @staticmethod
    def colour_from_temperature(temp_feels_like: int) -> str:
        """
        In clear or cloudy conditions we need to check the temp for the colour.
        """
        if temp_feels_like > 30:  # Hot
            weather_colour = "red"
        elif 21 < temp_feels_like < 30:  # Warm
            weather_colour = "orange"
        else:  # Cold
            weather_colour = "blue"
        return weather_colour
