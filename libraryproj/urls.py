"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from books import views

urlpatterns = [
    path("accounts/", include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='user_profile'),
    path('accounts/signup/', views.user_signup, name="user_signup"),
    path('admin/', admin.site.urls),
    path('ksiazki/', views.list_books),  #/ksiazki
    path('', views.my_page, name="main_page"),
    path('form/', views.form, name="form"),

    path("lista-ksiazek/<int:book_id>", views.book_details, name="book_details"),

    path("recenzje", views.ReviewList.as_view(), name="review_list"),

    path("autorzy", views.AuthorList.as_view(), name="author_list"),
    path("autorzy/<int:pk>", views.AuthorDetail.as_view(), name="author_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
