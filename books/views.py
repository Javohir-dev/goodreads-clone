from django.shortcuts import render
from django.views import View

from books.models import Book


class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            "books": books,
        }
        
        return render(request, 'books/list.html', context)
    

class BooksDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            "book": book,
        }

        return render(request, 'books/detail.html', context)
