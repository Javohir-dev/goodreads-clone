from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book


class BooksView(ListView):
    template_name = 'books/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class BooksDetailView(DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = 'id'
    model = Book


# class BooksView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         context = {
#             "books": books,
#         }
        
#         return render(request, 'books/list.html', context)
    

# class BooksDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         context = {
#             "book": book,
#         }

#         return render(request, 'books/detail.html', context)
