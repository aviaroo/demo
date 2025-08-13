import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(1, "Test User", "test@example.com", "beginner")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.user_type, "beginner")
        self.assertEqual(user.progress_history, [])

    def test_add_progress_record(self):
        user = User(1, "Test User", "test@example.com", "beginner")
        user.add_progress_record("Finished 100m freestyle")
        self.assertEqual(len(user.progress_history), 1)
        self.assertEqual(user.progress_history[0], "Finished 100m freestyle")

if __name__ == '__main__':
    unittest.main()
