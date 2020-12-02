from student import Student
from coursebookmark import CourseBookmark
from course import Course


# Requirement: 4.1.2. Bookmarked Courses
# The system shall have a Bookmarked Courses section which only lists all the courses bookmarked by the student.
def test_get_all_bookmarked_courses_for_student():
    student = Student()
    student.student_id = 100
    student.populate_course_bookmarks()

    # count of all bookmarked courses in the database for student_id = 100
    db_bookmarked_course_count = 5

    assert student.get_bookmarked_course_count() == db_bookmarked_course_count, \
        "Number of bookmarked courses for student with id 100 do not match database records."


# Requirement: 4.1.3. Watched Courses
# The system shall have a Watched Courses section which only lists all the courses that the student
# has either completed and/or has started watching.
def test_get_all_watched_courses_for_student():
    student = Student()
    student.student_id = 100
    student.populate_lesson_item_progress()

    # count of all watched courses in the database for student_id = 100
    db_watched_course_count = 5

    assert student.get_watched_course_count() == db_watched_course_count, \
        "Number of watched courses for student with id 100 do not match database records."


def test_add_course_bookmark():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    assert len(student.course_bookmarks) == 0, "Student must not have any bookmarks currently"

    course_bookmark = CourseBookmark()
    course_bookmark.course_id = course.course_id
    course_bookmark.student_id = student.student_id

    student.add_course_bookmark(course_bookmark)

    # student has no course bookmark on the course
    assert len(student.course_bookmarks) == 1, "Student must have 1 bookmark"


def test_remove_course_bookmark():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    assert len(student.course_bookmarks) == 0, "Student must not have any bookmarks currently"

    course_bookmark = CourseBookmark()
    course_bookmark.course_id = course.course_id
    course_bookmark.student_id = student.student_id

    student.add_course_bookmark(course_bookmark)

    assert len(student.course_bookmarks) == 1, "Student must have 1 bookmark"

    student.remove_course_bookmark(course_bookmark)
    assert len(student.course_bookmarks) == 0, "Student must have 0 bookmarks now after removing the bookmark"
