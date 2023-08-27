from django.urls import path
from books.views import (
    BooksView, 
    BooksDetailView, 
    AddReviewView, 
    EditReviewView, 
    DeleteReviewView,
    ConfirmDeleteReviewView,
)

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="books_list"),
    path("<int:id>/", BooksDetailView.as_view(), name="book_detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="reviews"),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit_review"),
    path("<int:book_id>/reviews/<int:review_id>/delete/confirm/", ConfirmDeleteReviewView.as_view(), name="confirm_delete_review"),
    path("<int:book_id>/reviews/<int:review_id>/delete/", DeleteReviewView.as_view(), name="delete_review"),
]
