from django.urls import path
from .views import health, BookList

urlpatterns = [
    path("health/", health, name="health"),
    path("books/", BookList.as_view(), name="book-list"),
]
