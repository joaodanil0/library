from django.urls import path
from user import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("login_validation", views.login_validation, name="login_validation"),
    path("register/", views.register, name="register"),
    path("register_validation", views.register_validation, name="register_validation"),
    path("logout/", views.logout, name="logout"),
]