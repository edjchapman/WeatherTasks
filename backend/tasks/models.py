import logging

from django.db import models

from tasks.services.weather_api import WeatherApi

logger = logging.getLogger(__name__)


class Task(models.Model):
    """
    To-do list task model.
    """
    description = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    weather_colour = models.CharField(max_length=50)
    temperature = models.FloatField(default=0)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.set_weather()
        super().save(*args, **kwargs)

    def set_weather(self):
        wa = WeatherApi(city=self.nearest_city)
        self.weather_colour = wa.get_weather_colour()
        self.temperature = wa.get_temp_feels_like()

    def get_weather_colour_display(self):
        return self.weather_colour if self.complete else WeatherApi(city=self.nearest_city).get_weather_colour()

    def get_temperature_display(self):
        return self.temperature if self.complete else WeatherApi(city=self.nearest_city).get_temp_feels_like()
