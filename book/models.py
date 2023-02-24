from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30)
    register_date = models.DateField()
    borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=30)
    borrow_date = models.DateTimeField()
    borrow_return = models.DateTimeField()
    borrow_time = models.DateField()
