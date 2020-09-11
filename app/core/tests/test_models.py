from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating new user with email is successful"""
        email = 'abc@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating superuser with email"""
        user = get_user_model().objects.create_superuser(
            email='ab@gmail.com',
            password='test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
