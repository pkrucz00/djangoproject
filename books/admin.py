from django.contrib import admin

# Register your models here.
from books.models import Book
from books.models import Author


admin.site.register(Book)
admin.site.register(Author)