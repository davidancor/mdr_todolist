from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = [
	{
		'title': 'task 1',
	},
	{
		'title': 'task 2',
	},
	{
		'title': 'task 3',
	},
	{
		'title': 'task 4',
	},
	{
		'title': 'task 5',
	},
]

def home(request):
	
	context = {
		'tasks': tasks
	}
	return render(request, "todolist_app/home.html", context)

def archive(request):
	return render(request, "todolist_app/archive.html")