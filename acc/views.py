import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required
def register_req(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()        
    return render(request,'acc/register.html',{'form':form})


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    return render(request,"acc/login.html",{'form':form})      

@login_required
def logout_req(request):
    logout(request)
    return redirect('login')      