from django.urls import path
from django.db import router

from rest_framework.routers import DefaultRouter

from .controller import CategoryViewSet, AuthorViewSet, BookViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
urlpatterns = router.urls


urlpatterns += [
    # path('', controller.index, name='index'),
    # path('author/<int:author_id>', controller.author, name='author'),
    # path('category/<int:category_id>', controller.category, name='category')
]