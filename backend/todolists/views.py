from django.views.generic import ListView

from todolists.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    queryset = Task.objects.all()
