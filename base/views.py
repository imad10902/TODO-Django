from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(host=request.user) #tasks for the logged in user get displayed
    else:
        tasks = None

    context = {'tasks': tasks}
    return render (request, 'base/home.html', context)




def addTask(request):
    form = TaskForm() #

    if request.method == 'POST':
        form = TaskForm(request.POST) #Instance for Task class with values from submission
    if form.is_valid():
        task = form.save(commit=False) 
        task.host = request.user #Task added for the logged in user
        task.save()
        return redirect('home')

    context = {'form': form}
    return render (request, 'base/add_task.html', context)





def updateTask(request, pk):
    task = Task.objects.get(id=pk) #Get the task to be deleted using its id
    form = TaskForm(instance=task) 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form':form}
    return render(request, 'base/add_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'base/delete.html')

def deleteAll(request):
    tasks = Task.objects.filter(host=request.user) #Get all tasks of the user to delete them all

    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html')


def loginPage(request):
    page = 'login' #to tell the "login_register" html to show login form or register form
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username) #Check if username exists
        except:
            messages.error(request, "No username found")

        user = authenticate(username=username, password=password) #Authenticate the user and password to provide user

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password dont match any user")


    return render(request, 'base/login_register.html', {'page':page})

def registerPage(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An Error occured")

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
