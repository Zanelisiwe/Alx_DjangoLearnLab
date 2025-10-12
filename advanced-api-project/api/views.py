from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Combined List + Create
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Anyone can read, only auth users can write

# Combined Retrieve + Update + Delete
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Anyone can read, only auth users can update/delete
