class Workout:
    def __init__(self, workout_id, title, description, target_swimmer_type):
        self.workout_id = workout_id
        self.title = title
        self.description = description
        self.parts = []
        self.target_swimmer_type = target_swimmer_type  # 'beginner', 'competitive', or 'all'

    def add_part(self, distance, stroke, details=""):
        self.parts.append({
            "distance": distance,
            "stroke": stroke,
            "details": details
        })

    def __repr__(self):
        return f"Workout({self.workout_id}, {self.title}, {self.target_swimmer_type})"
