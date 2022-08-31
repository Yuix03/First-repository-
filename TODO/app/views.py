from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *


def todo(request):
    if request.method == 'POST':
        a = request.POST.get('title')
        b = request.POST.get('time')
        c = request.POST.get('dec')
        d = request.POST.get('status')
        Todo.objects.create(title=a, time=b, description=c, status=d, user=request.user)
        return redirect('/todo/')
    if request.user.is_authenticated:
        data = {
            'todo': Todo.objects.filter(user=request.user)
        }
        return render(request, 'todo.html', data)
    else:
        return redirect('/login/')


def delete(request, a):
    Todo.objects.get(id=a).delete()
    return redirect('/todo/')


def login_view(request):
    log = request.POST.get('u')
    passw = request.POST.get('p')
    user = authenticate(username=log, password=passw)
    if request.method == "POST":
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/todo/')





    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')
def salom(hello):
    print('salom')