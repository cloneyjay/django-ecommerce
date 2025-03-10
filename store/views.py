from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def about(request):
    return render(request,'store/about.html', {})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_detail.html', {'product': product})


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
    return redirect('store:home')

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Successfull Registration.You are now logged in")
            return redirect('store:home')
        else:
            messages.success(request, "There was a problem registering your account")
            return redirect('store:register')
    else:
        return render(request,'store/register.html', {'form': form})

def category(request, categoryname):
    #Replace - with space
    categoryname = categoryname.replace('-', ' ')
    try:
        #Get the category
        category = Category.objects.get(name=categoryname)
        #Get all products in the category
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products': products, 'category': category})
    except:
        messages.error(request, "Category does not exist")
        return redirect('store:home')

    