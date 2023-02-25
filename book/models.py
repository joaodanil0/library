from django.db import models
from datetime import date
from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True)
    register_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=30, blank=True)
    borrow_date = models.DateTimeField(blank=True, null=True)
    borrow_return = models.DateTimeField(blank=True, null=True)
    borrow_time = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

