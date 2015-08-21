from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Creator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from article import views
# Create your views here.

def login_view(request):
    return render(request, 'creator/login.html')

def check_login_user(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect(views.index)
        else:
            context={'error':"invalid user"}
            return render(request, 'creator/login.html',context)
    else:
        return redirect(login_view)

def create_acc_view(request):
    return render(request, 'creator/create_account.html')

def add_creator_view(request):
    name = request.POST['name']
    username=request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        user = User.objects.create_user(first_name=name, username=username, password=password)
        user.save()
        return redirect(login_view)
    else:
        return redirect(create_acc_view)

def logout_acc_view(request):
    logout(request)
    return redirect(login_view)
