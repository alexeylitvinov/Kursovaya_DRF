from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user@test.com', password='12345')
        self.habit = Habit.objects.create(action='Поесть', time='14:00', place='Обед', periodicity=1, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тест создания привычки"""
        data = {'action': 'Поесть', 'time': '09:00', 'place': 'Завтрак', 'periodicity': 1}
        url = reverse('habits:create_habit')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': 2,
            'action': 'Поесть',
            'time': '09:00:00',
            "pleasant_habit": False,
            'place': 'Завтрак',
            "reward": None,
            'periodicity': 1,
            "action_time": 120,
            'is_public': False,
            "associated_habit": None,
            'user': 1
        })
        self.assertTrue(Habit.objects.all().exists())
        self.assertEqual(Habit.objects.count(), 2)

    def test_get_habit(self):
        """Тест получения привычки"""
        url = reverse('habits:detail_habit', kwargs={'pk': self.habit.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': 3,
            'action': 'Поесть',
            'time': '14:00:00',
            "pleasant_habit": False,
            'place': 'Обед',
            "reward": None,
            'periodicity': 1,
            "action_time": 120,
            'is_public': False,
            "associated_habit": None,
            'user': 2
        })

    def test_habit_list(self):
        """Тест получения списка привычек"""
        url = reverse('habits:habits')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 1)

    def test_habit_update(self):
        """Тест обновления привычки"""
        data = {'action': 'Попить', 'time': '08:00', 'place': 'Кухня', 'periodicity': 2}
        url = reverse('habits:update_habit', kwargs={'pk': self.habit.pk})
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), 'Попить')
        self.assertEqual(data.get('time'), '08:00:00')
        self.assertEqual(data.get('place'), 'Кухня')
        self.assertEqual(data.get('periodicity'), 2)

    def test_habit_delete(self):
        """Тест удаления привычки"""
        url = reverse('habits:delete_habit', kwargs={'pk': self.habit.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.all().exists())
