from django.shortcuts import render
from books.models import Book, Author, Review
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView


def hello_world(request):
    return render(request, template_name="hello.html")

def my_page(request):
    return render(request, template_name="index.html")

def form(request):
    return render(request, template_name="form.html")

def list_books(request):
    books = Book.objects.all()
    context123 = {
        "klucz": "wartosc",
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context123)

def book_details(request, book_id):
    book_from_database = Book.objects.get(pk=book_id)
    return render(request,
                  template_name="book_details.html",
                  context={"book_in_context": book_from_database})

def profile_view(request):
    return render(request, template_name="registration/profile.html")

def user_signup(request):
    if request.method == "POST":
        #przetwarzamy dane nowego uzytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        #wyswietlamy swiezy formularz
        form = UserCreationForm()

    return render(request, template_name="registration/signup_form.html",
                  context={"form": form})

class UserSignup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup_form.html"


class AuthorList(ListView):
    model = Author
    template_name = "books/author_list.html"

class ReviewList(ListView):
    model = Review

class AuthorDetail(DetailView):
    model = Author

class ReviewDetail(DetailView):
    model = Review