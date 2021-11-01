from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView

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


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["complete"]

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.pk})
