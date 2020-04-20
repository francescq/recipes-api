from django.test import TestCase
from django.urls import reverse
from rest_framework import status


from rest_framework.test import APIClient


PING_URL = reverse('ping')


class TestPing(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_should_return_pong(self):
        print(PING_URL)
        res = self.client.get(PING_URL)

        print(res)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
