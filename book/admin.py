from django.contrib import admin
from book.models import Book, Category, Borrow

# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Borrow)