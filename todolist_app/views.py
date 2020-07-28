from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
	if request.method=='POST':
		task=Task(title=request.POST['title'])
		task.save()
		return redirect('todolist_home')
	else:
		context = { 
			'tasks': Task.objects.all() 
			}
		return render(request, "todolist_app/home.html", context)

def archive(request):
	return render(request, "todolist_app/archive.html")

def deleteTask(request, task_id):
	task=Task.objects.filter(id=task_id)
	task.delete()
	return redirect('todolist_home')