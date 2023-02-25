from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from user.models import User
from hashlib import sha256

# Create your views here.

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def login_validation(request):
    name = request.POST.get("name")
    pwd = request.POST.get("password")

    hash_pwd = sha256(pwd.encode()).hexdigest()

    user = User.objects.filter(name = name).filter(password = hash_pwd)

    if not user:
         return redirect('/user/login/?status=1')
    
    request.session['usr'] = user[0].id
    return redirect(f'/system/home/?id_usuario={request.session["usr"]}')

def register(request):
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})

def register_validation(request):
    name = request.POST.get("name")
    pwd = request.POST.get("password")
    email = request.POST.get("email")

    if len(name) == 0 or len(email) == 0 or len(pwd) == 0:
        return redirect('/user/register/?status=2')

    try:       
        hash_pwd = sha256(pwd.encode()).hexdigest()
        user = User(name=name, password=hash_pwd, email=email)
        user.save()
        return redirect('/user/login/?status=0')
    except:
        return redirect('/user/register/?status=1')

def logout(request):
    request.session.flush()
    return redirect('/user/login')
