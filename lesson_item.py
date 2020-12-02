class LessonItem:

    def __init__(self, title, sort_id):
        self.lesson_item_id = 0
        self.title = title
        self.description = ''
        self.start_time = 0
        self.end_time = 0
        self.page_url = ''
        self.video_url = ''
        self.sort_id = sort_id

    def get_lesson_item_by_id(self, lesson_item_id):
        return None
