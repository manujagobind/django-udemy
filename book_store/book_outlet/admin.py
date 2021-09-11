from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    readonly_fields = ('slug',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)