class User:
    def __init__(self, user_id, name, email, user_type):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.user_type = user_type  # 'beginner' or 'competitive'
        self.progress_history = []

    def add_progress_record(self, record):
        self.progress_history.append(record)

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.user_type})"
