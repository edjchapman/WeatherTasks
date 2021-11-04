import random

from django.test import TestCase

from tasks.form_data.cities import cities
from tasks.models import Task


class TaskModelTestCase(TestCase):
    """
    Task model tests.
    """

    def test_weather_and_temperature_gets_set_on_save(self):
        t = Task()
        t.description = "Eat Ice Cream"
        t.nearest_city = random.choice(cities)
        t.save()
        self.assertGreater(t.temperature, 0)
        self.assertIn(t.weather_colour, ["orange", "blue", "red"])
