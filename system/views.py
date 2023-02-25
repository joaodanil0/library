from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from user.models import User
from book.models import Book, Borrow
from book.forms import RegisterBook
# Create your views here.


def home(request):
    session = request.session.get('usr')
    if session:
        user = User.objects.get(id=session)
        book = Book.objects.filter(user=user)
        form = RegisterBook()
        return render(request, 'home.html', {'books': book, 'logged':session, 'form':form})
    else:
        return redirect('/user/login/?status=2')

def book_info(request, id):
    session = request.session.get('usr')

    if session:
        book = Book.objects.get(id=id)
        if session == book.user.id:
            borrow = Borrow.objects.filter(book=book)
            form = RegisterBook()
            return render(request, 'book_info.html', {'book': book, 'borrows':borrow, 'logged':session, 'form':form})
        else:
            return render(request, "home.html")
    
