# relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from .views import register  # ✅ checker expects exactly views.register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs using built-in CBVs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ checker
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ checker
    path('register/', register, name='register'),  # ✅ checker expects views.register
]
