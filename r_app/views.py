from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def login_user(request):
    #check to see if login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged....")
            return redirect('login')
        else:
            messages.success(request, "There was an error please try again later....")
            return redirect('login')
    else:
        # return redirect('login.html')
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have succefully logout.......")
    return redirect("login")

def signup(request):
    return render(request, "signup.html", {})

