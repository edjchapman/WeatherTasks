from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView

from todolists.models import Task


class TaskListView(View):
    template_name = "todolists/task_list.html"
    context_object_name = 'task_list'

    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        return render(request, self.template_name, {"task_list": task_list})

    def post(self, request, *args, **kwargs):
        description = request.POST.get("description")
        if description:
            Task.objects.create(description=description)
        return redirect("task_list")


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["complete"]

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.pk})
