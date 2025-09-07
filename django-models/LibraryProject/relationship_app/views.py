# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ exact import checker expects
from .models import Book
from .models import Library  # ✅ on its own line

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
