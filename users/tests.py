from django.urls import reverse
from rest_framework import status

from users.models import User
from rest_framework.test import APITestCase


class UsersAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user@test.com', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_get_users(self):
        url = reverse('users:user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_users(self):
        data = {'email': 'test_user@test.com', 'password': '12345'}
        url = reverse('users:user')
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
