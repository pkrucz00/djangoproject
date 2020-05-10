from django.shortcuts import render
from books.models import Book

def hello_world(request):
    return render(request, template_name="hello.html")

def my_page(request):
    return render(request, template_name="index.html")

def list_books(request):
    books = Book.objects.all()
    context123 = {
        "klucz": "wartosc",
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context123)