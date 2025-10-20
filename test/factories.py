"""
Test Factory to create fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake Product instances for testing"""

    class Meta:
        """Associates this factory with the Product model"""
        model = Product

    product_id = factory.Sequence(lambda n: n)
    # Add code here to generate fake Products
