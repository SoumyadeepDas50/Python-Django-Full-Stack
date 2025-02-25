from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard') # Redirect to a dashboard or home page
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,'person/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'person/dashboard.html')

def date_time_view(request):
    return render(request,'person/index.html')


