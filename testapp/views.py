from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import signUpForm
from  django.contrib import messages

def register(request):
    if request.method=='POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created Successfully!!!")
            form.save()
    else:
        form=signUpForm()
    return render(request, 'testapp/sign_up.html',{'form':form})

def user_login(request):
    if request == "POST":
        fm=AuthenticationForm(request=request,data=request.post)
        if fm.is_valid():
            uname=fm.cleaned_data('username')
            upass=fm.cleaned_data('password')
            user=authenticate(uname,upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request , 'testapp/login.html',{'form':fm})