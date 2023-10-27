# cart/tests.py
from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def client():
    return APIClient()

def test_create_cart(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.force_authenticate(user=user)
    response = client.post('/carts/', {'user': user.id}, format='json')
    assert response.status_code == status.HTTP_201_CREATED

def test_get_cart_list(client):
    response = client.get('/carts/')
    assert response.status_code == status.HTTP_200_OK

# Добавьте другие тесты по необходимости
    