from django.db.models import Avg
from django.shortcuts import render

from .models import Book


def index(request):

    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))

    return render(request, 'book_outlet/index.html', {
        'books': books,
        'book_count': num_books,
        'avg_rating': avg_rating['rating__avg']
    })


def book_detail(request, slug):

    book = Book.objects.get(pk=slug)
    return render(request, 'book_outlet/book-detail.html', {
        'book': book
    })