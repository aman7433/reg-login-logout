# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django  import forms
class signUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm password')
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'email'}