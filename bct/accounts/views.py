from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task


# Create your views here.
def register(request):
    if request.method=="POST":
        username =request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image=request.FILES.get('image')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"user already exists")
            return redirect('register')
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
            
        )
        if image:
            Task.objects.create(
                user=user,
                image=image
            )
        messages.success(request,"Registration Successfully")
        return redirect('login')


    return render(request,'register.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')


    return render(request,'login.html')


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        title=request.POST.get('title')
        if title:
            Task.objects.create(user=request.user,title=title)
    tasks=Task.objects.filter(user=request.user)
    return render(request,'dashboard.html', {'tasks': tasks})


def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('dashboard')

def complete_task(request, id):
    task=Task.objects.get(id=id)
    task.completed=not task.completed
    task.save()
    return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect('login')