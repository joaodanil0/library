from django.shortcuts import render
from django.http import HttpResponse
from book.forms import RegisterBook

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterBook(request.POST)

        if form.is_valid():
            form.save()
            HttpResponse("Saved")
        else:
            return HttpResponse(form)