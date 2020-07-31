from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	if request.method=='POST':
		task=Task(title=request.POST['title'])
		task.save()
		return redirect('todolist_home')
	
	if request.method=='GET': 
		context = { 
			'tasks' : Task.objects.filter(is_archive=False)
			# 'tasks': Task.objects.all() 
			}
		return render(request, "todolist_app/home.html", context)

def archive(request):
	context = { 
		'tasks' : Task.objects.filter(is_archive=True)
	}
	return render(request, "todolist_app/archive.html", context)
	

def deleteTask(request, task_id):
	last_url=request.POST.get('last_url')
	task=Task.objects.filter(id=task_id).first()
	task.delete()
	return redirect(last_url)

def archiveTask(request, task_id):
	task=Task.objects.filter(id=task_id).first()
	task.is_archive=True
	task.save()
	messages.success(request, f'a task has been archived')
	return redirect ('todolist_home')

def unArchiveTask(request, task_id):
	task=Task.objects.filter(id=task_id).first()
	task.is_archive=False
	task.save()
	messages.success(request, f'A task has been Unarchived')
	return redirect ('todolist_archive')

def updateTask (request,task_id):
	task=Task.objects.filter(id=task_id).first()
	task.title=request.POST['title']
	task.save()
	return redirect ('todolist_home')