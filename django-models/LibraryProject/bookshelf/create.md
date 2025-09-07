# Create Operation

```python
from bookshelf.models import Book

# Create a new Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
