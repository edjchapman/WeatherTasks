from django.shortcuts import render

from todolists.models import TodoList


def todo_lists(request):
    context = {
        "todo_lists": TodoList.objects.all()
    }
    return render(request, "lists.html", context)
