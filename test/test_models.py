"""
Test cases for Product Model

Run all tests with:
    nosetests
    coverage report -m

For debugging only these tests:
    nosetests --stop tests/test_models.py:TestProductModel
"""
import os
import logging
import unittest
from decimal import Decimal
from service.models import Product, Category, db
from service import app
from tests.factories import ProductFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)


######################################################################
#  P R O D U C T   M O D E L   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
class TestProductModel(unittest.TestCase):
    """Test cases for Product model"""

    @classmethod
    def setUpClass(cls):
        """Runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Product.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """Runs once after the entire test suite"""
        db.session.close()

    def setUp(self):
        """Runs before each test"""
        db.session.query(Product).delete()  # Clean up previous tests
        db.session.commit()

    def tearDown(self):
        """Runs after each test"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_a_product(self):
        """Create a product and assert its attributes"""
        product = Product(
            name="Fedora",
            description="A red hat",
            price=12.50,
            available=True,
            category=Category.CLOTHS
        )
        self.assertEqual(str(product), "<Product Fedora id=[None]>")
        self.assertIsNotNone(product)
        self.assertIsNone(product.id)
        self.assertEqual(product.name, "Fedora")
        self.assertEqual(product.description, "A red hat")
        self.assertTrue(product.available)
        self.assertEqual(product.price, 12.50)
        self.assertEqual(product.category, Category.CLOTHS)

    def test_add_a_product(self):
        """Create a product and add it to the database"""
        products = Product.all()
        self.assertEqual(products, [])

        product = ProductFactory()
        product.id = None
        product.create()

        # Assert that it was assigned an id and appears in the database
        self.assertIsNotNone(pro
