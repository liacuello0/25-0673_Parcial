import pytest
import requests

URL = "https://dummyjson.com"

def test_get_all_products():
    response = requests.get(f"{URL}/products")
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

def test_get_single_product():
    product_id = 1
    response = requests.get(f"{URL}/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id

def test_create_product():
    new_product = {"title": "Test Product", "price": 100}
    response = requests.post(f"{URL}/products/add", json=new_product)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new_product["title"]
    assert data["price"] == new_product["price"]

def test_update_product():
    update_data = {"price": 150}
    response = requests.put(f"{URL}/products/1", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == update_data["price"]

def test_delete_product():
    response = requests.delete(f"{URL}/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["isDeleted"] is True

def test_get_image():
    response = requests.get(f"{URL}/image/300x300")
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("image/")
