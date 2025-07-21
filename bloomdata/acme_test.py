import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_attributes():
    prod = Product('Test Product')
    assert prod.price == 10
    assert prod.weight == 20
    assert prod.flammability == 0.5


def test_stealability_and_explode():
    prod = Product('Test Product', price=10, weight=20, flammability=0.5)
    assert prod.stealability() == 'Kinda stealable.'
    assert prod.explode() == '...boom!'


def test_generate_products_length():
    products = generate_products()
    assert len(products) == 30
    assert all(isinstance(p, Product) for p in products)


def test_generated_product_names():
    products = generate_products()
    for prod in products:
        adjective, noun = prod.name.split()
        assert adjective in ADJECTIVES
        assert noun in NOUNS
