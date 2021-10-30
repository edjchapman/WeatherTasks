from django.test import TestCase

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
