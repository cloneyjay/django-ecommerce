from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def about(request):
    return render(request,'store/about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('store:home')
        else:
            messages.success(request, "Invalid credentials")
            return redirect('store:login')
    else:
        return render(request,'store/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('home')
