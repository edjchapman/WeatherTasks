from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    """
    Task model admin.
    """
    model = Task
