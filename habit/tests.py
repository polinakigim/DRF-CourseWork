from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.models import User
from habit.models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@example.com", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.pleasant_habit = Habit.objects.create(
            owner=self.user,
            action="Послушать музыку",
            is_habit_nice=True,
            duration=60,
            periodicity=1
        )

        self.valid_data = {
            "action": "Сделать зарядку",
            "duration": 60,
            "periodicity": 1
        }

    def test_create_habit_success(self):
        url = reverse("habit:habit_create")
        response = self.client.post(url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_create_with_prize_and_related_fails(self):
        url = reverse("habit:habit_create")
        data = self.valid_data.copy()
        data["prize"] = "Шоколадка"
        data["is_related"] = self.pleasant_habit.pk
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Нельзя одновременно указывать", str(response.data))

    def test_create_with_nonpleasant_related_fails(self):
        not_pleasant = Habit.objects.create(
            owner=self.user, action="Уборка", is_habit_nice=False, duration=30, periodicity=1
        )
        url = reverse("habit:habit_create")
        data = self.valid_data.copy()
        data["is_related"] = not_pleasant.pk
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Связанная привычка должна быть приятной", str(response.data))

    def test_create_pleasant_with_prize_fails(self):
        url = reverse("habit:habit_create")
        data = self.valid_data.copy()
        data["is_habit_nice"] = True
        data["prize"] = "Конфета"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Приятная привычка не может иметь", str(response.data))

    def test_create_with_duration_over_limit_fails(self):
        url = reverse("habit:habit_create")
        data = self.valid_data.copy()
        data["duration"] = 180  # > 120 сек
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Время выполнения привычки", str(response.data))

    def test_create_with_zero_periodicity_fails(self):
        url = reverse("habit:habit_create")
        data = self.valid_data.copy()
        data["periodicity"] = 0
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Периодичность должна быть", str(response.data))

    def test_habit_list(self):
        url = reverse("habit:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_habit_retrieve(self):
        url = reverse("habit:habit_retrieve", args=[self.pleasant_habit.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.pleasant_habit.pk)

    def test_habit_update(self):
        url = reverse("habit:habit_update", args=[self.pleasant_habit.pk])
        data = {"action": "Новая привычка"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pleasant_habit.refresh_from_db()
        self.assertEqual(self.pleasant_habit.action, "Новая привычка")

    def test_habit_delete(self):
        url = reverse("habit:habit_delete", args=[self.pleasant_habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(pk=self.pleasant_habit.pk).exists())
