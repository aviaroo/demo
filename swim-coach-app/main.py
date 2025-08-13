import datetime
from models.user import User
from models.workout import Workout
from models.schedule import Schedule

def main():
    # Create a user
    user1 = User(1, "Alice", "alice@example.com", "beginner")
    print(f"Created User: {user1}")

    # Create a workout
    workout1 = Workout(101, "Beginner's Freestyle", "Focus on basic freestyle technique.", "beginner")
    workout1.add_part(200, "Freestyle", "Warm-up")
    workout1.add_part(400, "Freestyle", "Main set: 4 x 100m")
    workout1.add_part(100, "Kick", "Cool-down")
    print(f"Created Workout: {workout1}")
    print(f"Workout Parts: {workout1.parts}")


    # Schedule the workout for the user
    today = datetime.date.today()
    schedule1 = Schedule(1001, user1.user_id, workout1.workout_id, today)
    print(f"Created Schedule: {schedule1}")

    # Simulate completing the workout
    schedule1.complete_workout()
    print(f"Schedule status after completion: {schedule1.status}")


if __name__ == "__main__":
    main()
