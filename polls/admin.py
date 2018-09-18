from django.contrib import admin
from .models import Question, Choice
# Tutorial admin:
# user: admin
# pw: a
# email: admin@example.com
# Register your models here.
admin.site.register(Question)
