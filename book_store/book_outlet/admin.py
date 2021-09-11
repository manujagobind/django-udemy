from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    readonly_fields = ('slug',)


admin.site.register(Book, BookAdmin)