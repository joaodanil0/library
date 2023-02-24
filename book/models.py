from django.db import models
from datetime import date

# Create your models here.

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
