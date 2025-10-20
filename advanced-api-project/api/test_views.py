from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """Unit tests for Book API endpoints, ensuring CRUD operations,
    filtering, searching, and permissions work as expected.
    """

    def setUp(self):
        """Set up initial test data and authentication."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # Common URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # ----------------------------------------------------------------------
    # READ TESTS
    # ----------------------------------------------------------------------
    def test_list_books(self):
        """Ensure all books are listed."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_retrieve_book_detail(self):
        """Ensure a single book can be retrieved by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # ----------------------------------------------------------------------
    # CREATE TESTS
    # ----------------------------------------------------------------------
    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book."""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create a book."""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------------------------------------------------
    # UPDATE TESTS
    # ----------------------------------------------------------------------
    def test_update_book_authenticated(self):
        """Ensure authenticated users can update a book."""
        self.client.login(username='testuser', password='testpass')
        data = {"title": "Updated Title", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        """Ensure unauthenticated users cannot update a book."""
        data = {"title": "Fail Update", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------------------------------------------------
    # DELETE TESTS
    # ----------------------------------------------------------------------
    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete a book."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """Ensure unauthenticated users cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------------------------------------------------
    # FILTERING / SEARCH / ORDERING TESTS
    # ----------------------------------------------------------------------
    def test_filter_books_by_title(self):
        """Ensure filtering works using the title query parameter."""
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_search_books_by_title(self):
        """Ensure search functionality works."""
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_order_books_by_year(self):
        """Ensure ordering works."""
        Book.objects.create(title="Older Book", publication_year=2015, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
