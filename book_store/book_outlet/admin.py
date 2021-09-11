from django.contrib import admin
from django.db import models

from .models import Author, Book, Address


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    readonly_fields = ('slug',)


admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)