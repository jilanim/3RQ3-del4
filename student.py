class Student:

    def __init__(self):
        self.student_id = 0
        self.subscription = None
        self.invoices = None
        self.lesson_item_progress = []
        self.course_notes = []
        self.course_bookmarks = []

    def populate_lesson_item_progress(self):
        return None

    def populate_course_notes(self):
        return None

    def populate_course_bookmarks(self):
        return None

    def get_bookmarked_course_count(self):
        return None

    def get_watched_course_count(self):
        return None

    def add_course_bookmark(self, course_bookmark):
        return None

    def remove_course_bookmark(self, course_bookmark):
        return None

    def has_course_bookmark(self):
        return False
