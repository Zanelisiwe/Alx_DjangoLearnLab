# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Must import Library explicitly

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library detail with all books
class LibraryDetailView(DetailView):
    model = Library  # ✅ DetailView must use Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
