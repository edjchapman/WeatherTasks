from django.urls import reverse
from django.views.generic import ListView, CreateView

from todolists.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    queryset = Task.objects.all()


class TaskCreateView(CreateView):
    model = Task
    fields = ["description"]

    def get_success_url(self):
        return reverse("task_list")
