from django.urls import path
from user import views

urlpattern = [
    path("login/", views.login)
]