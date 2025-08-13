import unittest
import datetime
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.schedule import Schedule

class TestSchedule(unittest.TestCase):

    def test_schedule_creation(self):
        today = datetime.date.today()
        schedule = Schedule(1, 101, 201, today)
        self.assertEqual(schedule.schedule_id, 1)
        self.assertEqual(schedule.user_id, 101)
        self.assertEqual(schedule.workout_id, 201)
        self.assertEqual(schedule.date, today)
        self.assertEqual(schedule.status, 'pending')

    def test_complete_workout(self):
        schedule = Schedule(1, 101, 201, datetime.date.today())
        schedule.complete_workout()
        self.assertEqual(schedule.status, 'completed')

    def test_miss_workout(self):
        schedule = Schedule(1, 101, 201, datetime.date.today())
        schedule.miss_workout()
        self.assertEqual(schedule.status, 'missed')

if __name__ == '__main__':
    unittest.main()
