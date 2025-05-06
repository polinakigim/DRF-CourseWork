from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

User = get_user_model()

class UserModelTest(TestCase):

    def test_create_user_successfully(self):
        user = User.objects.create_user(email="test@example.com", password="securepass", tg_chat_id="12345")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("securepass"))
        self.assertEqual(user.tg_chat_id, "12345")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_successfully(self):
        admin_user = User.objects.create_superuser(email="admin@example.com", password="adminpass", tg_chat_id="99999")
        self.assertEqual(admin_user.email, "admin@example.com")
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

    def test_email_is_unique(self):
        User.objects.create_user(email="unique@example.com", password="pass", tg_chat_id="123")
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email="unique@example.com", password="pass", tg_chat_id="456")

    def test_str_returns_email(self):
        user = User.objects.create_user(email="strtest@example.com", password="pass", tg_chat_id="000")
        self.assertEqual(str(user), "strtest@example.com")

    def test_username_field_is_email(self):
        self.assertEqual(User.USERNAME_FIELD, "email")
