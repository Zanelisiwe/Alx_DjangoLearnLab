from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# ------------------------------------------------------------
# ListView: Retrieve all books (Read-Only)
# Accessible to all users (unauthenticated and authenticated)
# Added filtering, searching, and ordering
# ------------------------------------------------------------
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Allow filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Allow searching by title and author
    search_fields = ['title', 'author']

    # Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


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
