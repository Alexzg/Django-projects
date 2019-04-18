from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.addTask, name='addTask'),
	path('complete/<task_id>', views.completeTask, name='completeTask'),
	path('delete/<task_id>', views.deleteTask, name='deleteTask'),
]