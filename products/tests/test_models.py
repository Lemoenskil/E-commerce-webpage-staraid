from django.test import TestCase
from products.models import Product, ProductSpecification

# Create your tests here.
class TestProducts(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name = "abs",
            description = "description1",
            long_description = "this is a lonnnnnng description",
            features = "feature 1 and feature 2",
            price = 2.45,
            featured = True,
            stock = 9,
            on_offer = False,  
        )
    
    def setUp(self):
        self.product = Product.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.product._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_name_label(self):
        self.assertLabelIs("name", "name")

    def test_description_label(self):
        self.assertLabelIs("description", "description")

    def test_long_description_label(self):
        self.assertLabelIs("long_description", "long description")

    def test_features_label(self):
        self.assertLabelIs("features", "features")

    def test_price_label(self):
        self.assertLabelIs("price", "price")

    def test_featured_label(self):
        self.assertLabelIs("featured", "featured")

    def test_stock_label(self):
        self.assertLabelIs("stock", "stock")

    def test_on_offer_label(self):
        self.assertLabelIs("on_offer", "on offer")

# Create your tests here.
class TestProductSpecification(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(
            name = "abs",
            description = "description1",
            long_description = "this is a lonnnnnng description",
            features = "feature 1 and feature 2",
            price = 2.45,
            featured = True,
            stock = 9,
            on_offer = False,  
        )
        ProductSpecification.objects.create(
            product = product,
            name = "name",
            value = "value",
        )
    
    def setUp(self):
        self.productSpecification = ProductSpecification.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.productSpecification._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_name_label(self):
        self.assertLabelIs("name", "name")

    def test_value_label(self):
        self.assertLabelIs("value", "value")

    def test_order_label(self):
        self.assertLabelIs("order", "order")
