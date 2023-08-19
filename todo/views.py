from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task = request.POST["task"]
    Task.objects.create(task=task)
    return redirect("home")


def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_complted = True
    task.save()
    return redirect("home")


def mark_as_undone(request, id):
    task = Task.objects.get(id=id)
    task.is_complted = False
    task.save()
    return redirect("home")


def edit_task(request, id):
    get_task = Task.objects.get(id=id)

    if request.method == 'POST':  # Here we fixed the attribute name to be all lowercase
        new_task = request.POST["task"]
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:
        context = {
            "get_task": get_task
        }

        return render(request, "edit-task.html", context)

def delete_task(request, id):
    task_to_delete = get_object_or_404(Task, id=id)  
    task_to_delete.delete()  
    return redirect('home')


