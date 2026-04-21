from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class CalculatorAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('calculate')

    def test_add_api(self):
        data = {"operation": "add", "a": 10, "b": 5}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 15)

    def test_divide_by_zero_api(self):
        data = {"operation": "divide", "a": 10, "b": 0}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_sqrt_api(self):
        data = {"operation": "sqrt", "a": 25}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 5.0)

    def test_missing_operand_api(self):
        data = {"operation": "add", "a": 10}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('b', response.data)

    def test_invalid_operation_api(self):
        data = {"operation": "invalid", "a": 10, "b": 5}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
