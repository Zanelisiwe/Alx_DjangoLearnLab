# relationship_app/urls.py

from django.urls import path
from .views import list_books
from .views import LibraryDetailView  # ✅ import on its own line

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
]
