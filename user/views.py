from django.shortcuts import render
from django.http import HttpResponse
from user.models import User

# Create your views here.

def login(request):
    return HttpResponse("login")

def register(request):
    return render(request, 'register.html')

def register_validation(request):
    name = request.POST.get("name")
    pwd = request.POST.get("password")
    email = request.POST.get("email")

    user = User(name=name, password=pwd, email=email)
    user.save()
    return HttpResponse(f'{name} {pwd} {email}')