from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from user.models import User

# Create your views here.


def home(request):
    session = request.session.get('usr')
    if session:
        user = User.objects.get(id=session)
        return HttpResponse(f"System Hello {user.name}")
    else:
        return redirect('/user/login/?status=2')