from django.test import TestCase
from django.utils.text import slugify

from todolists.models import TodoList, Task


class TodoListModelTestCase(TestCase):
    """
    TodoList model tests.
    """

    def test_a_todo_list_can_be_created_with_a_title(self):
        todo_list = TodoList.objects.create(title="Holiday List")
        self.assertEqual(
            "Holiday List",
            todo_list.title
        )

    def test_the_slug_field_is_populated_on_save(self):
        todo_list = TodoList.objects.create(title="Holiday List")
        self.assertEqual(
            slugify(todo_list.title)[:50],
            todo_list.slug
        )


class TaskModelTestCase(TestCase):
    """
    Task model tests.
    """

    def test_a_task_can_be_added_to_a_list(self):
        todo_list = TodoList.objects.create(title="Holiday List")
        Task.objects.create(todo_list=todo_list, description="Eat Ice Cream", nearest_city="Brighton")
        first_task = todo_list.tasks.first()
        self.assertEqual(
            first_task.description,
            "Eat Ice Cream"
        )
