from django.db import models
from django.utils.text import slugify


class TodoList(models.Model):
    """
    To-do list model.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title[:10]

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        self.slug = slugify(self.title)[:50]


class Task(models.Model):
    """
    To-do list task model.
    """
    todo_list = models.ForeignKey("todolists.TodoList", related_name="tasks", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"List=({self.todo_list.title[:10]}) Task=({self.description[:10]})"
