from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

class StartPageTests(TestCase):
	print("- StartPageTests")
	def test_start_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)
	def test_start_page_correct_url_by_name(self):
		response = self.client.get(reverse('index'))
		self.assertEquals(response.status_code, 200)
	def test_start_page_uses_correct_html(self):
		response = self.client.get(reverse('index'))
		self.assertContains(response, '<h1>Ucair - TodoApp</h1>')
	def test_start_page_uses_incorrect_html(self):
		response = self.client.get(reverse('index'))
		self.assertNotContains(response, '<h1>I have a wrong app</h1>')
	def test_form_data_entry_redirection(self):
		response = self.client.post('/add', {
			'title':'ViewTest-1', 'content':'Some description', 'category':'General', 'startDate':'2018-12-30', 'dueDate':'2018-12-29', })
		self.assertEquals(response.status_code, 302) #redirection

class AddTaskPageTests(TestCase):
	print("- AddTaskPageTests")
	def test_add_page_status_code(self):
		response = self.client.get('/add/')
		self.assertNotEquals(response.status_code, 200)
	def test_add_page_correct_url_by_name(self):
		response = self.client.get(reverse('addTask'))
		self.assertNotEquals(response.status_code, 200)