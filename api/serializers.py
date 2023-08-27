from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'comment', 'book', 'user')

