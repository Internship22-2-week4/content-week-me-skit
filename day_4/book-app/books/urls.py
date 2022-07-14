from django.urls import path
from . import controller


urlpatterns = [
    path('', controller.index, name='index'),
    path('author/<int:author_id>', controller.author, name='author'),
    path('category/<int:category_id>', controller.category, name='category')
]