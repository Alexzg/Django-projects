from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from .forms import SignupForm


# def signup(request):
#     path = "sign_up/sign_up_form.html"
#     return render(request, path)

def signup(request):
    path = "sign_up/sign_up_form.html"
    if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/loggedin/')
    else:
        form = SignupForm()
    return render(request, path, {'form':form})

def loggedin(request):
    path = "sign_up/logged_in.html"
    return render(request, path)
