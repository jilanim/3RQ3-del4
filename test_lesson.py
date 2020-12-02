from lesson import Lesson
from lesson_item import LessonItem


# Requirement: 4.4.1.1. Automatically play first video
# The system shall automatically start playing the first video in the course once the watch content page has
# finished loading all the content.
def test_get_first_lesson_item():
    lesson = Lesson("Learning HTML")

    lesson_items = [LessonItem("Basic HTML", 1), LessonItem("HTML Elements", 2), LessonItem("HTML Image Element", 3)]
    lesson.add_lesson_items(lesson_items)

    first_lesson_item_sort_id = lesson.get_first_lesson_item_sort_id()
    assert first_lesson_item_sort_id == 1, "The first lesson item's sort id must be 1"


# Requirement: 4.4.1.2. Automatically play next video
# The system shall automatically start playing the next video once the current video being watched finishes.

# Requirement: 4.4.1.3. Watching last video
# The system shall take no further action once the last video is completely watched and the video player
# shall come to a stop and play no more videos.
def test_get_next_lesson_item():
    lesson = Lesson("Learning HTML")

    lesson_items = [LessonItem("Basic HTML", 1), LessonItem("HTML Elements", 2), LessonItem("HTML Image Element", 3)]
    lesson.add_lesson_items(lesson_items)

    next_lesson_item_sort_id = lesson.get_next_lesson_item_sort_id(1)
    assert next_lesson_item_sort_id == 2, "The next lesson item's sort id must be 2"

    next_lesson_item_sort_id = lesson.get_next_lesson_item_sort_id(2)
    assert next_lesson_item_sort_id == 3, "The next lesson item's sort id must be 3"

    next_lesson_item_sort_id = lesson.get_next_lesson_item_sort_id(3)
    assert next_lesson_item_sort_id == -1, \
        "The current lesson item is the last one and the sort id must be -1 as there are no more lesson items"


# Requirement: 4.4.1.4. Switching to another video
# The system shall allow the student to switch to other videos in the course by clicking on any video
# title in the table of contents beside the video player.
def test_get_lesson_item_by_id():
    lesson = Lesson("Learning HTML")

    lesson_item = LessonItem('HTML Attributes', 5)
    lesson_item.lesson_item_id = 1000;

    lesson.add_lesson_item(lesson_item)

    lesson_item = lesson.get_lesson_item_by_id(1000)
    assert lesson_item is not None, "The lesson item with id 1000 exists and should have been found"
