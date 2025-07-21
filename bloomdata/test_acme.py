from bloomdata.acme import Product

def test_default_product_price():
    """Test default product price is 10."""
    prod = Product("Test Product")
    assert prod.price == 10

def test_default_weight():
    """Test default product weight is 20."""
    prod = Product("Heavy Product")
    assert prod.weight == 20

def test_identifier_is_7_digits():
    """Test that identifier is a 7-digit number."""
    prod = Product("ID Check")
    assert 1000000 <= prod.identifier <= 9999999
