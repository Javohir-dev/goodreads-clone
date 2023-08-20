from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from books.models import Book, BookReview

from books.forms import BookReviewForm


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 3)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            "page_obj": page_obj,
            "search_query": search_query,
        }

        return render(request, 'books/list.html', context)
    

class BooksDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context = {
            "book": book,
            "form": review_form,
        }

        return render(request, 'books/detail.html', context)


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        context = {
            "book": book,
            "form": review_form,
        }

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment'],
            )

            return redirect(reverse("books:book_detail", kwargs={"id": book.id}))
        
        return render(request, 'books/detail.html', context) 
