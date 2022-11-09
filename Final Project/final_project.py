from bakery_canvas import get_courses
from bakery import assert_equal


def count_courses(user_token: str) -> int:
    """
    This function counts the number of courses being taken by the user.

    Args:
        user_token (str): The user that is having their courses counted.
    Return:
        int: The number of courses counted.
    """

    courses = get_courses(user_token)
    count = 0
    for course in courses:
        count += 1
    return count


assert_equal(count_courses("annie"), 6)
assert_equal(count_courses("jeff"), 6)
assert_equal(count_courses("pierce"), 0)
assert_equal(count_courses("troy"), 1)


def find_cs1(user_token: str) -> int:
    """
    This function finds the first course that has the text "CISC1" in the code field given the user_token
    Args:
        user_token (str): The user that is having their courses counted.

    Returns:
        int: The ID number of the first course that has "CISC1" in it.
    """

    courses = get_courses(user_token)
    if not courses:
        return 0

    course_id = 0
    for course in courses:
        if "CISC1" in course.code:
            course_id = course.id
            break

    return course_id


assert_equal(find_cs1("annie"), 100167)
assert_equal(find_cs1("jeff"), 100167)
assert_equal(find_cs1("pierce"), 0)
assert_equal(find_cs1("troy"), 0)


def find_course(user_token: str, course_id: int) -> str:
    """
    This function finds the course ids from a user and returns the full name of the course

    Args:
        user_token (str): The user token of the user in question.
        course_id (int): The unique course ID.

    Returns:
        str: The full name of the course.
    """

    course_name = "no course found"
    courses = get_courses(user_token)
    for course in courses:
        if course.id == course_id:
            course_name = course.name

    return course_name


assert_equal(find_course("annie", 394382), "History of Ice Cream")
assert_equal(find_course("jeff", 134088), "Physical Education Education")
assert_equal(find_course("pierce", 12345), "no course found")
assert_equal(find_course("troy", 394382), "History of Ice Cream")


def render_courses(user_token: str) -> str:
    """
    This function takes in the courses of a user, and renders in them in a way to make them readable
    Args:
        user_token (str): The user that is looking for the course render

    Returns:
        str: A formatted string representing the course ID and code.
    """

    courses = get_courses(user_token)
    course_render = ""

    for course in courses:
        course_render += f"{course.id}: {course.code}\n"

    return course_render


annie_courses = "679554: MATH101\n386814: ENGL101\n4182: SPAN101\n394382: ICRM304\n100167: CISC1\n134088: PHED201\n"


jeff_courses = "679554: MATH101\n386814: ENGL101\n4182: SPAN101\n394382: ICRM304\n100167: CISC1\n134088: PHED201\n"

pierce_courses = ""

troy_courses = "394382: ICRM304\n"

assert_equal(render_courses("annie"), annie_courses)
assert_equal(render_courses("jeff"), jeff_courses)
assert_equal(render_courses("pierce"), pierce_courses)
assert_equal(render_courses("troy"), troy_courses)
