from django.contrib import admin
from books.models import Book, Author, BookAuthor, BookReview

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn")
    search_fields = ("title", "description")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("book", "author")
    search_fields = ("book", "author")


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "comment", "stars_given")
    search_fields = ("comment", "book", "stars_given")
    list_filter = ("stars_given", "user")
