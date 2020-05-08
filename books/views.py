from django.shortcuts import render
from books.models import Book

def hello_world(request):
    return render(request, template_name="hello.html")

def list_books(request):
    books = Book.objects.all()
    context = {
        "klucz": "wartosc",
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context)