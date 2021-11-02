from django.db import models


class Task(models.Model):
    """
    To-do list task model.
    """
    description = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description
