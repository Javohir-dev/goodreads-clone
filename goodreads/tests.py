from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):

    def test_paginated_list(self):
        book = Book.objects.create(title="Book3", description="description3", isbn="3215464533")
        self.client.post(
            reverse("users:register"),
            data={
                "username": "salmonxon123", 
                "first_name": "salmonxon", 
                "last_name": "Khamidullaev", 
                "email": "salmonxon.py@gmail.com", 
                "password": "somepassword"
            }
        )

        user = CustomUser.objects.get(username='salmonxon123')

        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, comment="some comment")
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, comment="some comment 4")
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment="some comment 5")

        response = self.client.get(reverse('home') + "?page_size2")

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)
