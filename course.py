class Course:

    def __init__(self):
        self.course_id = 0
        self.title = ''
        self.short_description = ''
        self.detailed_description = ''
        self.published_date = ''
        self.completion_time = 0
        self.lessons = []
        self.author = ''

    def add_course(self, title, short_description, detailed_description, published_date, completion_time, lessons, author):
        return None

    def populate_course_detail(self, course_id):
        return None

    def get_all_courses(self):
        return None

    def courses_count(self):
        return None

    def searchMatchCourseCount(self, search_text):
        return -1
