# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import SearchForm
from .forms import ExampleForm



# ---------- Book list / search (safe, ORM + validated input) ----------
def book_list(request):
    """
    Display all books with optional search.
    Uses Django ORM (prevents SQL injection) and validates input via SearchForm.
    """
    form = SearchForm(request.GET or None)
    qs = Book.objects.all()
    if form.is_valid() and form.cleaned_data.get("q"):
        qs = qs.filter(title__icontains=form.cleaned_data["q"])
    return render(request, "bookshelf/book_list.html", {"books": qs, "form": form})


# ---------- Create book (requires custom permission) ----------
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        year = request.POST.get("publication_year", "").strip()

        if title and author and year.isdigit():
            Book.objects.create(
                title=title,
                author=author,
                publication_year=int(year),
            )
            return redirect("bookshelf:book_list")

    return render(request, "bookshelf/book_form.html")


# ---------- Delete book (requires custom permission) ----------
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})


# ---------- Example form view (used by templates/bookshelf/form_example.html) ----------
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Example: create a Book from the form fields
            Book.objects.create(
                title=form.cleaned_data["title"],
                author=form.cleaned_data["author"],
                publication_year=0,  # or extend ExampleForm to include this field
            )
            return redirect("bookshelf:book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
