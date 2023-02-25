from django.urls import path
from system import views

urlpatterns = [
    path('home/', views.home, name='home'),
]