from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Category, Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {"books": books})


def author(request, author_id):
    author = Author.objects.get(id = author_id)
    return render(request, 'books/author.html', {"author": author})
    return HttpResponse('Autor ID: {}, nombre: {}'.format(author.id, author.first_name))


def category(request, category_id):
    cartegory = Category.objects.get(id = category_id)
    return HttpResponse('Category ID: {}, description: {}'.format(cartegory.id, cartegory.descriptioon))