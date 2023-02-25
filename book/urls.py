from django.urls import path
from book import views

urlpatterns = [
    path("register/", views.register, name="register_book")
]