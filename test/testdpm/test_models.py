import unittest
from datetime import datetime

from pydantic import SecretStr, ValidationError

from src.dpm.models.user import User


class TestUserModel(unittest.TestCase):
    def test_user_creation_valid(self):
        """Test creating a valid user."""
        user_data = {
            "user_id": 1,
            "username": "testuser",
            "password": "securepassword",
            "email": "testuser@example.com",
        }
        user = User(**user_data)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, "testuser")
        self.assertIsInstance(user.password, SecretStr)
        self.assertIsNotNone(user.created_at)
        self.assertIsNone(user.last_login)

    def test_user_id_invalid(self):
        """Test invalid user_id (non-positive)."""
        with self.assertRaises(ValidationError):
            User(
                user_id=-1,
                username="testuser",
                password="securepassword",
                email="testuser@example.com",
            )

    def test_username_invalid(self):
        """Test custom constraints for username."""
        with self.assertRaises(ValidationError):
            User(
                user_id=1,
                username="ab",  # Too short
                password="securepassword",
                email="testuser@example.com",
            )

    def test_email_invalid(self):
        """Test invalid email."""
        with self.assertRaises(ValidationError):
            User(user_id=1, username="testuser", password="securepassword", email="invalid-email")

    def test_datetime_values(self):
        """Test default values for created_at and last_login."""
        user = User(
            user_id=1, username="testuser", password="securepassword", email="testuser@example.com"
        )
        # Verify `created_at` is a valid ISO format
        self.assertTrue(datetime.fromisoformat(user.created_at))
