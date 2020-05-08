from django.db import models

def widok():
    return ...

class Book(models.Model):
    # id
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()
    author = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.title