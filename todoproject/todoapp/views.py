from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import *


def index(request):
    tasks = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)  # this line for adding into the list
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'forms': form}
    return render(request, 'todoapp/list.html', context)


def updateTask(request, pk):
    task1 = task.objects.get(id=pk)
    form = taskForm(instance=task1)
    if request.method == 'POST':
        form = taskForm(request.POST, instance=task1)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'todoapp/update.html', context)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todoapp/delete.html', context)

# Create your views here.
