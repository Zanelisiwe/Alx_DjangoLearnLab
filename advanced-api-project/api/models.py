from django.db import models

# Model representing an author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name  # Display author name in admin and shell

# Model representing a book
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'  # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return self.title  # Display book title in admin and shell
