from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_email_success(self):
        """Test creating a new user with an email is successful"""
        email = 'test@emaple.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@EXAMPLE.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with a invalid email raises error"""
        with self.assertRaises(ValueError):
            email = None
            password = 'Test123'
            get_user_model().objects.create_user(email, password)

    def test_creating_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_super_user(
            'testsuperuser@example',
            'Test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
