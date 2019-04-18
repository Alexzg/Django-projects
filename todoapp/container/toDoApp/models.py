from django.db import models

# SQLite3 database is used		

class TodoList(models.Model): 
	title = models.CharField(max_length=50)
	content = models.TextField(blank=True) 
	due_date = models.DateField()
	start_date = models.DateField()
	category = models.CharField(max_length=20)
	complete = models.BooleanField(default=False)