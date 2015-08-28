from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from article import views
from django.contrib import messages
from creator.forms import RegisterUserTest, CreateUser


def login_view(request):
    """view to  render creator/login.html"""
    return render(request, 'creator/login.html')


def check_login_user(request):
    """view to accept data from login form,authenticate user
        if success redirect to article  views.index_view
        if not render the creator/login.html"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(views.index_view)
        else:
            return redirect(login_view)
    else:
        messages.success(request, 'Username or password is invalid')
        return render(request, 'creator/login.html')


def create_acc_view(request):
    """view to render create_account.html"""
    return render(request, 'creator/create_account.html')


def add_creator_view(request):
    """view to accept data from create user form and create user"""
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            if password == repassword:
                user = User.objects.create_user(first_name=name, username=username, password=password)
                user.save()
                messages.success(request, 'New user created')
                return redirect(login_view)
            else:
                return redirect(create_acc_view)
    else:
        redirect(create_acc_view)


def logout_acc_view(request):
    """View to logout user"""
    logout(request)
    return redirect(login_view)


