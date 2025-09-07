# relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books, LibraryDetailView,
    register, login_view, logout_view,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    # Task 1: Book & Library
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Task 2: Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Task 3: Role-Based Access
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
