from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    year = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="books")

    def __str__(self):
        return self.title