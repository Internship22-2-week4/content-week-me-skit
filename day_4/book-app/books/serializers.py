# Django rest framework serializers 
from rest_framework import serializers
# models
from .models import Book, Author, Category
from user.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # Método 1 para mostrar datos de relación entre tablas
    # author = AuthorSerializer()
    # category = CategorySerializer()

    # Método 2
    # category = serializers.SlugRelatedField(
    #     many = False,
    #     read_only = True,
    #     slug_field = 'name'
    # )

    # author = serializers.SlugRelatedField(
    #     many = False,
    #     read_only = True,
    #     slug_field = 'first_name'
    # )   
    
    # Método 2.5
    # author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all())
    # category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    # user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())

    # Método 3


    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title', 'author', 'category']

    # Método 3
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'image': instance.image,
            'isbn': instance.isbn,
            'author': {
                'id': instance.author.id,
                'first_name': instance.author.first_name,
                'last_name': instance.author.last_name,
                'image': instance.author.image
            },
            'category': {
                'id': instance.category.id,
                'name': instance.category.name,
                'descripton': instance.category.descriptioon,
            }
        }
