from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from user.models import User
from book.models import Book, Borrow

# Create your views here.


def home(request):
    session = request.session.get('usr')
    if session:
        user = User.objects.get(id=session)
        book = Book.objects.filter(user=user)
        return render(request, 'home.html', {'books': book})
    else:
        return redirect('/user/login/?status=2')

def book_info(request, id):
    session = request.session.get('usr')

    if session:
        book = Book.objects.get(id=id)
        if session == book.user.id:
            borrow = Borrow.objects.filter(book=book)
            return render(request, 'book_info.html', {'book': book, 'borrows':borrow})
        else:
            return render(request, "home.html")
    
