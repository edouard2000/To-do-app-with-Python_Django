from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complted = False).order_by("-updated")
    complted_task = Task.objects.filter(is_complted = True).order_by("-updated")

    context = {
        "tasks": tasks,
        'complted_task' : complted_task
    }
    return render(request, "home.html", context)
