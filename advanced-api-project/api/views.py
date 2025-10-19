from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ------------------------------------------------------------
# ListView: Retrieve all books (Read-Only)
# Accessible to all users (unauthenticated and authenticated)
# ------------------------------------------------------------
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------------------------------------
# DetailView: Retrieve a single book by ID (Read-Only)
# Accessible to all users (unauthenticated and authenticated)
# ------------------------------------------------------------
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------------------------------------
# CreateView: Add a new book
# Only accessible to authenticated users
# ------------------------------------------------------------
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # You can customize creation behavior here
        serializer.save()


# ------------------------------------------------------------
# UpdateView: Modify an existing book
# Only accessible to authenticated users
# ------------------------------------------------------------
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Customize update behavior or validation
        serializer.save()


# ------------------------------------------------------------
# DeleteView: Remove a book
# Only accessible to authenticated users
# ------------------------------------------------------------
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
