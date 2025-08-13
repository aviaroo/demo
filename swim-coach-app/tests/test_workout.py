import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.workout import Workout

class TestWorkout(unittest.TestCase):

    def test_workout_creation(self):
        workout = Workout(1, "Test Workout", "A workout for testing", "all")
        self.assertEqual(workout.workout_id, 1)
        self.assertEqual(workout.title, "Test Workout")
        self.assertEqual(workout.description, "A workout for testing")
        self.assertEqual(workout.target_swimmer_type, "all")
        self.assertEqual(workout.parts, [])

    def test_add_part(self):
        workout = Workout(1, "Test Workout", "A workout for testing", "all")
        workout.add_part(100, "Freestyle", "Warm-up")
        self.assertEqual(len(workout.parts), 1)
        self.assertEqual(workout.parts[0]["distance"], 100)
        self.assertEqual(workout.parts[0]["stroke"], "Freestyle")
        self.assertEqual(workout.parts[0]["details"], "Warm-up")

if __name__ == '__main__':
    unittest.main()
