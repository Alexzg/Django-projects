from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
