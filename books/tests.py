from django.test import TestCase
from django.urls import reverse

from books.views import BooksView, BooksDetailView
from books.models import Book

class BooksTestCase(TestCase):

    def test_no_book(self):
        response = self.client.get(reverse("books:books_list"))

        self.assertContains(response, "No books found.")

    def testbooks_list(self):
        Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        Book.objects.create(title="Book2", description="description2", isbn="3215464522")
        Book.objects.create(title="Book3", description="description3", isbn="3215464533")

        response = self.client.get(reverse("books:books_list"))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        response = self.client.get(reverse("books:book_detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
        self.assertContains(response, book.isbn)