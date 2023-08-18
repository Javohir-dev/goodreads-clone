from django.test import TestCase
from django.urls import reverse

from books.views import BooksView, BooksDetailView
from books.models import Book

class BooksTestCase(TestCase):

    def test_no_book(self):
        response = self.client.get(reverse("books:books_list"))

        self.assertContains(response, "No books found.")


    def testbooks_list(self):
        book1 = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        book2 = Book.objects.create(title="Book2", description="description2", isbn="3215464522")
        book3 = Book.objects.create(title="Book3", description="description3", isbn="3215464533")

        response = self.client.get(reverse("books:books_list") + "?page_size=2")
        for book in [book1, book2]:
            self.assertContains(response, book.title)
            self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:books_list") +"?page=2&page_size=2")
        self.assertContains(response, book3.title)


    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        response = self.client.get(reverse("books:book_detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
        self.assertContains(response, book.isbn)

    def test_search_books(self):
        book1 = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        book2 = Book.objects.create(title="Book2", description="description2", isbn="3215464522")
        book3 = Book.objects.create(title="Book3", description="description3", isbn="3215464533")

        response = self.client.get(reverse("books:books_list") + "?q=book1")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)
        response = self.client.get(reverse("books:books_list") + "?q=book2")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)
        response = self.client.get(reverse("books:books_list") + "?q=book3")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)
