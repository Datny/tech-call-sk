"""
Tests for recipe APIs.
"""

from core.models import Products

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

FILTERED_PRODUCTS_URL = reverse('recipe:recipe-list')


class PrivateRecipeApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()


    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes."""

        res = self.client.get(FILTERED_PRODUCTS_URL)

        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
