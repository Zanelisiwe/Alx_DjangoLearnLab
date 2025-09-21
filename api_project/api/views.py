from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets  # ← add viewsets

from .models import Book
from .serializers import BookSerializer


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Book via DRF router.
    """
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
