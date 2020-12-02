from course_note import CourseNote


# Requirement: 4.5.1. Add a note
# The system shall allow the student to add a note to the course while watching a video from the course.
# The text input should be restricted up to 300 characters in length with a minimum of 5 characters required.
def test_validate_course_note():
    course_note = CourseNote(1, 100, "")
    course_note.note = "shor"

    assert len(course_note.note) >= 5, "Note must be at least 5 characters in length"

    course_note.note = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. " \
                       "Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus " \
                       "mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat " \
                       "massa quis enim. Doneccc"

    assert len(course_note.note) <= 300, "Note must be less than or equal to 300 characters in length"
