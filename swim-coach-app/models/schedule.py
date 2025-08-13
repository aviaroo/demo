import datetime

class Schedule:
    def __init__(self, schedule_id, user_id, workout_id, date):
        self.schedule_id = schedule_id
        self.user_id = user_id
        self.workout_id = workout_id
        self.date = date
        self.status = 'pending'  # 'pending', 'completed', 'missed'

    def complete_workout(self):
        self.status = 'completed'

    def miss_workout(self):
        self.status = 'missed'

    def __repr__(self):
        return f"Schedule({self.schedule_id}, User: {self.user_id}, Workout: {self.workout_id}, Date: {self.date})"
