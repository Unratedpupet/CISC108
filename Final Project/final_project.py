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
