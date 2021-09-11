from django.urls import path

from .views import index, book_detail


urlpatterns = [
    path('<slug:slug>', book_detail, name='book-detail'),
    path('', index, name='index')
]