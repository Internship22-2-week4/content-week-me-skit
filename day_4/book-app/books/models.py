from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptioon = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
