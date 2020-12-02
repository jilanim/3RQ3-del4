from course import Course


# Requirement: 4.1. Listing courses
# The system shall allow a student to view a list of all courses.
def test_get_all_courses():
    course = Course()
    course.get_all_courses()

    # count of all courses in the database
    db_courses_count = 10

    assert course.courses_count() == db_courses_count, "Course list should contain all %s courses." % db_courses_count


# Requirement: 4.1.1. List all courses
def test_course_has_short_description():
    course = Course()
    course.populate_course_detail(111)

    assert len(course.short_description) > 0, "Course must have a short description"


# Requirement: 4.2.1.1. Course Details Content
def test_course_has_detailed_description():
    course = Course()
    course.populate_course_detail(111)

    assert len(course.detailed_description) > 0, "Course must have a detailed description"


# Requirement: 4.1.1. List all courses
# Requirement: 4.2.1.1. Course Details Content
def test_course_has_common_course_details():
    course = Course()
    course.populate_course_detail(111)

    assert len(course.title) > 0, "Course must have a title"
    assert len(course.author) > 0, "Course must have an author"
    assert len(course.published_date) > 0, "Course must have a published date"
    assert len(course.completion_time) > 0, "Course must have completion time"


# Requirement: 4.2.1.1. Course Details Content
def test_course_has_additional_details():
    course = Course()
    course.populate_course_detail(111)

    assert len(course.lessons) > 0, "Course must have lessons"


# Requirement: 4.1.4. Course search filter
# The system shall allow a student to search for a course using a search filter that would lookup up the search text across the course title and description.
def test_course_search():
    course = Course()
    course.add_course('Intro to CSS', 'This is an intro course to CSS',
                      'In this course you will learn all about CSS and how you use it to make your site look amazing',
                      '01/11/2020', 120, [], 'John Doe')

    matched_course_count = course.searchMatchCourseCount('CSS')

    assert matched_course_count > 0, "The added course should have matched the search criteria using the 'CSS' keyword"
