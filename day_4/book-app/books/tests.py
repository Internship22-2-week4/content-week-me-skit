from django.test import TestCase
from .models import Author, Category, Book

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(name='Test', descriptioon='This is a test', status=True)


    def test_category_name_is_iqual_test(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Test')


    def test_category_name_is_not_empty(self):
        category = Category.objects.get(id=1)
        self.assertIsNot(category.name, '')