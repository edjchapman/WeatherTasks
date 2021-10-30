from django.contrib import admin

from todolists.models import TodoList, Task


class TaskModelInline(admin.StackedInline):
    """
    Task model inline.
    """
    model = Task
    extra = 0


@admin.register(TodoList)
class TodoListModelAdmin(admin.ModelAdmin):
    """
    TodoList model admin.
    """
    inlines = [
        TaskModelInline
    ]
