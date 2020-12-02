class LessonItemProgress:

    def __init__(self, progress_id, student_id, is_completed):
        self.progress_id = progress_id
        self.student_id = student_id
        self.lesson_item_id = 0
        self.watched_time = 0
        self.is_completed = is_completed
