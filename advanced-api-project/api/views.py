from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

# List all books
class BookListView(ListView):
    model = Book
    template_name = "books_list.html"

# Show details of a single book
class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

# Create a new book (login required)
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = "book_form.html"

# Update an existing book (login required)
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = "book_form.html"

# Delete a book (login required)
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = "/books/"
    template_name = "book_confirm_delete.html"
