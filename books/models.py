from django.db import models

def widok():
    return ...

class Book(models.Model):
    # id
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()

    author = models.ManyToManyField(to="books.Author",
                                    verbose_name="autorzy",
                                    related_name="books")

    class Meta:
        ordering = ["title"]
        verbose_name = "książka"
        verbose_name_plural = "książki"

    def __str__(self):
        return "Książka: " + self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField(verbose_name="o autorze", blank=True)
    photo = models.ImageField(verbose_name="zdjęcie", blank=True)