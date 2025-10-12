from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),       # GET list, POST create
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-delete'),  # GET, PUT, DELETE
]
