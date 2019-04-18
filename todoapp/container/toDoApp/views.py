from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from toDoApp.models import TodoList


def index(request): 
	tasks = TodoList.objects.all() 
	return render(request, "index.html", {"tasks": tasks})

@require_POST
def addTask(request): 
	title = request.POST["title"]
	content = request.POST["content"]
	due_date = str(request.POST["dueDate"])
	start_date = str(request.POST["startDate"])
	category = request.POST["category"]
	task = TodoList(title=title, content=content, due_date=due_date, start_date=start_date, category=category)
	task.save()
	return redirect('index')

def completeTask(request, task_id):
	task = TodoList.objects.get(pk=task_id) 
	task.complete = True 
	task.save()
	return redirect('index')

def deleteTask(request, task_id):
	task = TodoList.objects.get(pk=task_id) 
	task.delete()
	return redirect('index')