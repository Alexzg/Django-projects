from django.urls import path

from . import views

app_name = "sign_up"
urlpatterns = [
    path('', views.signup, name='sign_up_form'),
    path('signup/', views.signup, name='sign_up_form'),
    path('loggedin/', views.loggedin, name='loggedin')
]
