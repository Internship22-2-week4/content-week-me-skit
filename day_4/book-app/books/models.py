from django.db import models
from user.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptioon = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title