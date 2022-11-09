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
