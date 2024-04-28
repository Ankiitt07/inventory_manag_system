import json
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

def register(request):
    return render(request, "signup/register.html")
    
def login_page(request):
    return render(request, "signup/login.html")

def register_new_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username already exist')
            return redirect('register')

        new_data_created = User.objects.create(
            username = username,
            first_name = first_name
        )
        new_data_created.set_password(password)
        new_data_created.save()
        return redirect("login")
    else:
        return render(request, "signup/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')

def user_logout(request):
    if User.is_authenticated:
        logout(request)
        return redirect("login")