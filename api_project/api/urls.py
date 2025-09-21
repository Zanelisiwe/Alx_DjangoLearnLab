from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # ← add this import
from .views import health, BookList, BookViewSet

router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    path("health/", health, name="health"),
    path("books/", BookList.as_view(), name="book-list"),
    path("auth/token/", obtain_auth_token, name="obtain-token"),  # ← add this
    path("", include(router.urls)),
]
