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

    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:    
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request , 'testapp/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    return render(request,'testapp/profile.html',{'name':request.user})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')