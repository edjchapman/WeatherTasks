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

    def test_weather_colour_display_method_does_not_update_after_the_task_is_complete(self):
        t = Task()
        t.description = "Eat Ice Cream"
        t.nearest_city = random.choice(cities)
        t.complete = True
        t.save()
        Task.objects.update(weather_colour="black")
        t.refresh_from_db()
        self.assertEqual(t.get_weather_colour_display(), "black")

    def test_temperature_display_method_does_not_update_after_the_task_is_complete(self):
        t = Task()
        t.description = "Eat Ice Cream"
        t.nearest_city = random.choice(cities)
        t.complete = True
        t.save()
        Task.objects.update(temperature=8000)
        t.refresh_from_db()
        self.assertEqual(t.get_temperature_display(), 8000)
