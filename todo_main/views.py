from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complted = False)
    context = {
        "tasks": tasks
    }
    return render(request, "home.html", context)
