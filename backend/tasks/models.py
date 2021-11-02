import logging

import requests
from django.db import models

from config.settings import OPEN_WEATHER_API_KEY

logger = logging.getLogger(__name__)


class Task(models.Model):
    """
    To-do list task model.
    """
    description = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    weather_colour = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.set_weather()
        super().save(*args, **kwargs)

    def set_weather(self):
        if not self.complete:
            weather_id = self.get_weather_id(city=self.nearest_city)
            self.weather_colour = self.get_weather_colour(weather_id=weather_id)

    @staticmethod
    def get_weather_id(city: str) -> int:
        """
        Make API call for weather for the neaarest city.
        Return the first weather group digit.
        """
        group = 0
        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_API_KEY}"
            )
            response = r.json()
            group_id = response["weather"][0]["id"]
            group = int(str(group_id)[:1])
        except Exception as e:
            logger.exception(f"Problem getting weather group: {e}")
        return group

    @staticmethod
    def get_weather_colour(weather_id=0):
        weather_colour = "white"
        try:
            weather_colour = {
                0: "white",
                2: "blue",  # Thunderstorm
                3: "orange",  # Drizzle
                5: "red",  # Rain
                6: "red",  # Snow
                7: "red",  # Atmosphere
                8: "red"  # Clear
            }[weather_id]
        except Exception as e:
            logger.exception(f"Problem getting weather colour: {e}")
        return weather_colour
