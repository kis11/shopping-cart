from app.shopping_cart import to_usd, calc_tax, find_price
import os
import pandas


def test_to_usd():
    result = to_usd(3)
    assert result == "$3.00"

def test_calc_tax():
    result = calc_tax(100)
    assert result == "8.75"

def test_find_price():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]
    products = pandas.DataFrame(products)
    assert find_price(products,3) == 2.49


