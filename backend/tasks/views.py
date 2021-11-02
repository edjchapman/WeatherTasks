from django.shortcuts import render, redirect
from django.views import View

from tasks.models import Task


class TaskListView(View):
    """
    View to handle adding and listing tasks.
    """
    template_name = "tasks/task_list.html"
    context_object_name = 'task_list'

    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        return render(request, self.template_name, {"task_list": task_list})

    def post(self, request, *args, **kwargs):
        description = request.POST.get("description")
        if description:
            Task.objects.create(description=description)
        return redirect("task_list")


class TaskDetailView(View):
    """
    View to handle updating individual tasks.
    """
    template_name = "tasks/task_detail.html"
    context_object_name = 'task_detail'

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get("pk"))
        return render(request, self.template_name, {"task": task})

    def post(self, request, *args, **kwargs):
        complete = request.POST.get("complete")
        task = Task.objects.get(id=kwargs.get("pk"))
        if complete:
            task.complete = True if complete == "true" else False
            task.save()
        return render(request, self.template_name, {"task": task})
