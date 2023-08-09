from django.urls import path
from books.views import BooksView, BooksDetailView

app_name = "books"
urlpatterns = [
    path('', BooksView.as_view(), name='books_list'),
    path('<int:id>/', BooksDetailView.as_view(), name='book_detail'),
]
