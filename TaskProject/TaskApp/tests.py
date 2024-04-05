from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .views import home  # Replace ".views" with the actual path to your views.py

class HomeViewTest(APITestCase):

    def test_get_courses(self):
        url = reverse('home')  # Get the URL for the view using reverse
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "demo_id": 123,
            "demo_title": "Demo Title",
            "demo_decsription": "This is demo description",
            "demo_status": "Demo Status"
        })

    def test_post_allowed(self):
        url = reverse('home')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_not_allowed(self):
        url = reverse('home')
        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
