from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.forms import RegisterBook

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/system/home')
        else:
            return HttpResponse(form)