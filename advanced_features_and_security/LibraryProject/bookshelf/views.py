from django.shortcuts import render

# Create your views here.
# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book


# ---------- Book list view ----------
def book_list(request):
    """
    Display all books.
    """
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# ---------- Create book view ----------
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


# ---------- Delete book view ----------
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("bookshelf:book_list")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

# ---------- Request book view ----------
def book_list(request):
    form = SearchForm(request.GET or None)
    qs = Book.objects.all()
    if form.is_valid() and form.cleaned_data.get("q"):
        qs = qs.filter(title__icontains=form.cleaned_data["q"])  # ORM param -> no SQL injection
    return render(request, "bookshelf/book_list.html", {"books": qs, "form": form})