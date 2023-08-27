from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookAuthor, Author
from users.models import CustomUser

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

    def test_book_author(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        author = Author.objects.create(first_name="javohir", last_name="khamidullaev", email="javohir@gmail.com", bio="bio")
        book_author = BookAuthor.objects.create(book=book, author=author)
        response = self.client.get(reverse("books:book_detail", kwargs={"id": book.id}))

        self.assertContains(response, book_author.author.full_name())
        self.assertEqual(book_author.author.full_name(), "javohir khamidullaev")


class BookReviewsTestCase(TestCase):
    
    def test_add_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        user = CustomUser.objects.create(
            username="javohir.coder",
            first_name="javohir",
            last_name="nimadur",
            email="javohir@gmail.com",
        )
        user.set_password("somepassword")
        user.save()
        self.client.login(username="javohir.coder", password="somepassword")

        self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={
            "stars_given": 3,
            "comment": "somecomment",
        })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, "somecomment")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)

    def test_add_wrong_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        user = CustomUser.objects.create(
            username="javohir.coder",
            first_name="javohir",
            last_name="nimadur",
            email="javohir@gmail.com",
        )
        user.set_password("somepassword")
        user.save()
        self.client.login(username="javohir.coder", password="somepassword")

        self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={
            "stars_given": 6,
            "comment": "somecomment",
        })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 0)
        self.assertNotEqual(book_reviews.count(), 1)

    # def test_edit_review(self):
    #     book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
    #     user = CustomUser.objects.create(
    #         username="javohir.coder",
    #         first_name="javohir",
    #         last_name="nimadur",
    #         email="javohir@gmail.com",
    #     )
    #     user.set_password("somepassword")
    #     user.save()
    #     self.client.login(username="javohir.coder", password="somepassword")

    #     self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={
    #         "stars_given": 4,
    #         "comment": "somecomment",
    #     })
    #     book_reviews = book.bookreview_set.all()


