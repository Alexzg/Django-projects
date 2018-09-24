from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponseRedirect

from .models import User

def signup(request):
    path = "sign_up/sign_up_form.html"
    if request.method == 'POST':
        form = request.POST # Load the data from request to "form"
        firstname = form.get('firstname', default='No such field')
        lastname = form.get('lastname', default='No such field')
        email = form.get('email', default='No such field')
        pw = form.get('password', default='No such field')

        saved_users = User.objects.filter(name=firstname)
        try:
            User.objects.get(name=firstname) # Raises error if doesn't exist
            print("Already exist", saved_users)
        except: # Save new "user" in "model"
            User(
            name=firstname, surname=lastname,
            email=email, password=pw).save()
            print("New entry")
            return HttpResponseRedirect('/loggedin/')
    else:
        pass
    return render(request, path)

# https://docs.djangoproject.com/en/2.1/topics/auth/default/#how-to-log-a-user-in
# def login(request):
#     path = "sign_up/sign_up_form.html" # NEED TO CHAGNE
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to page
#     else:
#         # Return an 'invalid login' message
#     return render(request, path)

def loggedin(request):
    path = "sign_up/logged_in.html"
    return render(request, path)
