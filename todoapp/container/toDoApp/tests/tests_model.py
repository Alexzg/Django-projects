from django.test import TestCase

from toDoApp.models import TodoList as todos

class ToDoListTests(TestCase):
	print("- ToDoListTests")
	def setUp(self):
		todos.objects.create(
			title="Autotest-1", content="Some content...", category = "Work", due_date="2019-01-20", start_date="2019-01-22")
		todos.objects.create(
			title="Autotest-2", content="Some other content...", category = "Personal", due_date="2019-03-20", start_date="2019-03-22")

	def test_title_exist(self):
		task = todos.objects.get(id=1)
		expected_object_title = f'{task.title}'
		self.assertEquals(expected_object_title, 'Autotest-1')
		
	def test_content_exist(self):
		task = todos.objects.get(id=2)
		expected_object_content = f'{task.content}'
		self.assertEquals(expected_object_content, 'Some other content...')	