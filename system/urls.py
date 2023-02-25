from django.urls import path
from system import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('book_info/<int:id>', views.book_info, name="book_info"),
]