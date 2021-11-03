from django.shortcuts import render, redirect
from django.views import View

from tasks.form_data.cities import cities
from tasks.models import Task


class TaskListView(View):
    """
    View to handle adding and listing tasks.
    """
    template_name = "tasks/task_list.html"
    context_object_name = 'task_list'

    def get(self, request, *args, **kwargs):
        context = {
            "task_list": Task.objects.all(),
            "cities": sorted(cities)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        description = request.POST.get("description")
        city = request.POST.get("city")
        if city and description:
            t = Task()
            t.nearest_city = city
            t.description = description
            t.save()
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
        task = Task.objects.get(id=kwargs.get("pk"))
        action = request.POST.get("action")
        if action == "complete":
            task.complete = True
            task.save()
        if action == "save":
            task.description = request.POST.get("description")
            task.save()
        if action == "delete":
            task.delete()
            return redirect("task_list")
        return render(request, self.template_name, {"task": task})
