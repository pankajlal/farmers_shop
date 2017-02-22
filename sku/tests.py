from django.test import TestCase
from .models import SKU, SKUCategory
# Create your tests here.


class CommonSetup(TestCase):

    def setUp(self):
        SKUCategory.objects.create(name='grocery')
        SKUCategory.objects.create(name='fruits')
        SKUCategory.objects.create(name='vegetables')


class SKUCategoryTestCase(CommonSetup):

    def test_categories_created(self):
        gr = SKUCategory.objects.get(name='grocery')
        self.assertEqual(gr.name, 'grocery')


class SKUTestCase(CommonSetup):

    def test_sku_is_created(self):
        fruits = SKUCategory.objects.get(name='fruits')
        SKU.objects.create(name="Banana", category=fruits)
        sku = SKU.objects.get(name="Banana")

        self.assertEqual(sku.name, "Banana")
        self.assertEqual(sku.category.name, "fruits")
