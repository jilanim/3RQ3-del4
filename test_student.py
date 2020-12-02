from course_note import CourseNote
from student import Student
from coursebookmark import CourseBookmark
from course import Course
from lesson_item_progress import LessonItemProgress


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


# Requirement: 4.3.1. Add a bookmark
# The system shall bookmark the course when the icon is inactive and user clicks on the icon.
# The icon should change in color and look like an active UI control.
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
    assert len(student.course_bookmarks) == 1, "Student must have 1 bookmark"


# Requirement: 4.3.2. Remove a bookmark
# The system shall remove the bookmark on the course when the icon is active and user clicks on the icon.
# The icon should change in color and look like an inactive UI control.
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
    assert len(student.course_bookmarks) == 0, "Student must have 0 bookmarks after removing the bookmark"


# Requirement: 4.4.2. Continue watching
# The system shall allow the student to continue watching from the moment where they last stopped
# watching the videos. A Continue Watching button should be present on the course details page,
# if the user has previously watched content from the course.
def test_get_last_lesson_item_not_completed():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100
    # assert len(student.lesson_item_progress) > 0, "Student has not watched any courses yet."

    # populate student.lesson_item_progress
    student.lesson_item_progress.append(LessonItemProgress(1, student.student_id, True))
    student.lesson_item_progress.append(LessonItemProgress(2, student.student_id, False))

    lesson_item = student.get_last_lesson_item_not_completed(course.course_id)
    assert lesson_item is not None, "A lesson item should be available as student has watched courses " \
                                    "with incomplete lesson items"


# Requirement: 4.5. Note
# The system shall allow students to make notes on each course.
# This is an alternative to handwritten notes. Each student will see their own notes for each course
# and the notes will only be visible on the watch content page. The notes should be listed beside the video player
# with a UI control for accepting note input and a UI control for saving a new note or modifications to an
# existing note.
def test_get_all_course_notes():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    student.course_notes = [CourseNote(student.student_id, course.course_id, "Learning is great"),
                            CourseNote(student.student_id, course.course_id, "Learning is amazing")]

    course_notes = student.get_all_course_notes(course.course_id)
    assert course_notes is not None, "Course notes should be available as student has notes for course " \
                                     "with course id equal to 1"


# Requirement: 4.5.1. Add a note
# The system shall allow the student to add a note to the course while watching a video from the course.
# The text input should be restricted up to 300 characters in length with a minimum of 5 characters required.
def test_add_course_note():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    assert len(student.course_notes) == 0, "Student must not have any course notes currently"

    course_note = CourseNote(student.student_id, course.course_id, "Learning is great")
    student.add_course_note(course_note)

    assert len(student.course_notes) == 1, "Student must have 1 course note"


# Requirement: 4.5.2. Update a note
# The system shall allow the student to update the content of an existing note. 
# A UI control must be present beside each note to indicate that the note can be edited. 
# Clicking on the control should allow for modifications and for saving the note.
def test_update_course_note():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    assert len(student.course_notes) == 0, "Student must not have any course notes currently"

    course_note = CourseNote(student.student_id, course.course_id, "Learning is great")
    student.add_course_note(course_note)

    assert len(student.course_notes) == 1, "Student must have at least 1 course note to update"

    course_note.update_note("Learning is amazing")
    assert course_note.note == "Learning is amazing", "Should have received 'Learning is amazing' message"


# Requirement: 4.5.3. Remove a note
# The system shall allow the student to remove a note. A UI control must be present beside each note
# for removing the note.
def test_remove_course_note():
    course = Course()
    course.course_id = 1

    student = Student()
    student.student_id = 100

    assert len(student.course_notes) == 0, "Student must not have any course notes currently"

    course_note = CourseNote(student.student_id, course.course_id, "Learning is great")
    student.add_course_note(course_note)

    assert len(student.course_notes) == 1, "Student must have 1 course note to remove"

    student.remove_course_note(course_note)
    assert len(student.course_notes) == 0, "Student must have 0 course notes after removing the previous course note"
