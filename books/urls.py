from django.urls import path
from books.views import BooksView, BooksDetailView, AddReviewView

app_name = "books"
urlpatterns = [
    path('', BooksView.as_view(), name='books_list'),
    path('<int:id>/', BooksDetailView.as_view(), name='book_detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name="reviews"),
]
