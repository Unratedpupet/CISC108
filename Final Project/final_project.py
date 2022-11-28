from bakery_canvas import get_courses, get_submissions
from bakery import assert_equal
import matplotlib.pyplot as plt
import sys

# my_token = sys.argv[1]


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


def execute(command: str, user_token: str, course_id: int) -> int:
    """

    Args:
        command (str): The command that is inputted to choose what to do.
        user_token (str): The user that is being requested.
        course_id (int): The course ID

    Returns:
        int: The new course ID or the course ID that was passed in.
    """
    # Prints out the courses being taken by the user currently.
    print(render_courses(user_token))

    if command == "course":
        course_id = int(input("Please input a course ID: "))
        print(find_course(user_token, course_id))
        return course_id
    elif command == "exit":
        return 0
    else:
        return course_id


def main(user_token: str):
    """
    The main function that runs the commands
    Args:
        user_token (str): The user id of the user looking for data.

    Returns:
        None
    """
    if count_courses(user_token) == 0:
        print("No courses available")

    current_course_id = find_cs1(user_token)
    if current_course_id == 0:
        current_course_id = 1

    while current_course_id > 0:
        user_command = input("What would you like to do?\ncourse\nexit\nChoose: ")
        current_course_id = execute(user_command, user_token, current_course_id)


def total_points(user_token: str, course_id: int) -> int:
    """
    The function gets the total number of points possible for the course

    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        int: The total points possible for the course.
    """
    submissions = get_submissions(user_token, course_id)
    possible_points = 0
    for submission in submissions:
        possible_points += submission.assignment.points_possible
    return possible_points


assert_equal(total_points("annie", 679554), 420)
assert_equal(total_points("annie", 386814), 700)
assert_equal(total_points("annie", 100167), 1060)
assert_equal(total_points("jeff", 679554), 420)
assert_equal(total_points("jeff", 386814), 700)
assert_equal(total_points("troy", 394382), 100)


def count_comments(user_token: str, course_id: int) -> int:
    """
    This function produces an integer representing the number of comments across all the submissions for that course.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        int: The total number of comments across all the submission for the course
    """

    submissions = get_submissions(user_token, course_id)
    total_comments = 0

    for submission in submissions:
        for comment in submission.comments:
            total_comments += 1

    return total_comments


assert_equal(count_comments("annie", 679554), 14)
assert_equal(count_comments("annie", 100167), 33)
assert_equal(count_comments("troy", 394382), 0)


def ratio_graded(user_token: str, course_id: int) -> str:
    """
    Produces a string value representing the number of assignments that have been graded compared to the number of
    total assignments in the course.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        str: value representing the number of assignments that have been graded compared to the number of
            total assignments in the course.
    """

    submissions = get_submissions(user_token, course_id)
    total_assignments = 0
    graded_assignments = 0

    for submission in submissions:
        total_assignments += 1
        if submission.grade:
            graded_assignments += 1

    return f"{graded_assignments}/{total_assignments}"


assert_equal(ratio_graded("annie", 679554), "10/10")
assert_equal(ratio_graded("annie", 134088), "6/11")


def average_score(user_token: str, course_id: int) -> float:
    """
    Produces a float representing the average, unweighted score of all the assignments in the course.

    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        float: the average, unweighted score of all assignments in the course

    """

    submissions = get_submissions(user_token, course_id)

    total_possible = total_points(user_token, course_id)
    graded_score = 0
    for submission in submissions:
        if submission.grade:
            graded_score += submission.score

    return graded_score / total_possible


assert_equal(average_score("annie", 679554), 0.95)
assert_equal(average_score("annie", 386814), 0.97)
assert_equal(average_score("jeff", 386814), 0.7)


def average_weighted(user_token: str, course_id: int) -> float:
    """
    Produces a float representing the average, weighted score of all the assignments in the course.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        float: The average, weighted score of all the assignments in the course.
    """

    submissions = get_submissions(user_token, course_id)

    weighted_total = 0
    weighted_scored = 0

    for submission in submissions:
        if submission.grade:
            weighted_total += (
                submission.assignment.points_possible
                * submission.assignment.group.weight
            )
            weighted_scored += submission.score * submission.assignment.group.weight

    return weighted_scored / weighted_total


assert_equal(average_weighted("annie", 679554), 0.9471153846153846)
assert_equal(average_weighted("annie", 100167), 0.9750741839762611)
assert_equal(average_weighted("annie", 134088), 0.93841059602649)
assert_equal(average_weighted("jeff", 386814), 0.7)


def average_group(user_token: str, course_id: int, group_name: str) -> float:
    """
    The function returns a float representing the average, unweighted score for all the graded
    submissions that have that group_name.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID
        group_name (str): The name of the group

    Returns:
        float: the average, unweighted score for all the graded
            submissions that have that group_name.
    """

    group_name = group_name.capitalize()
    submissions = get_submissions(user_token, course_id)
    total_possible_points = 0
    total_points_scored = 0
    for submission in submissions:
        if submission.grade and submission.assignment.group.name == group_name:
            total_points_scored += submission.score
            total_possible_points += submission.assignment.points_possible

    if total_possible_points == 0:
        return 0.0
    else:
        return total_points_scored / total_possible_points


assert_equal(average_group("annie", 679554, "HOMEWORK"), 0.9636363636363636)
assert_equal(average_group("annie", 679554, "exam"), 0.935)


def render_assignment(user_token: str, course_id: int, assignment_id: int) -> str:
    """
    The function produces a string representing the assignment and its submission details.

    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID
        assignment_id (int): The assignment ID

    Returns:
        str: A render of assignment ID, group name, module name, and grade
            If no assignment found, returns 'Assignment not found'
    """

    submissions = get_submissions(user_token, course_id)

    assignment_name = ""
    group_name = ""
    module_name = ""
    assignment_grade = ""
    take = False

    for submission in submissions:
        if submission.assignment.id == assignment_id:
            assignment_name = f"{submission.assignment.name}"
            group_name = f"Group: {submission.assignment.group.name}"
            module_name = f"Module: {submission.assignment.module}"
            if submission.score:
                assignment_grade = f"Grade: {submission.score}/{submission.assignment.points_possible} ({submission.grade})"
            else:
                assignment_grade = "Grade: (missing)"
            take = True

    if take:
        return f"{assignment_id}: {assignment_name}\n{group_name}\n{module_name}\n{assignment_grade}"
    else:
        return f"Assignment not found: {assignment_id}"


assert_equal(render_assignment("annie", 679554, 7), "Assignment not found: 7")
assert_equal(
    render_assignment("annie", 679554, 299650),
    "299650: Introduction\nGroup: Homework\nModule: Module 1\nGrade: 10.0/10 (A)",
)
assert_equal(
    render_assignment("annie", 679554, 553716),
    "553716: Basic Addition\nGroup: Homework\nModule: Module 2\nGrade: 14.0/15 (A)",
)
assert_equal(
    render_assignment("annie", 679554, 805499),
    "805499: Basic Subtraction\nGroup: Homework\nModule: Module 2\nGrade: 19.0/20 (A)",
)
assert_equal(
    render_assignment("annie", 134088, 937202),
    "937202: Technology in the outdoor classroom\nGroup: Homework\nModule: Module 2\nGrade: (missing)",
)
assert_equal(
    render_assignment("jeff", 386814, 24048),
    "24048: HOMEWORK 3\nGroup: Assignments\nModule: MODULE 1\nGrade: 58.0/100 (F)",
)


def render_all(user_token: str, course_id: int) -> str:
    """
    Produces a single string that describes all the submissions in the course.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        str: A render of all the submission of the course

    """

    submissions = get_submissions(user_token, course_id)

    all_submissions = ""
    for submission in submissions:
        if submission.grade:
            all_submissions += (
                f"{submission.assignment.id}: {submission.assignment.name} (graded)\n"
            )
        else:
            all_submissions += (
                f"{submission.assignment.id}: {submission.assignment.name} (ungraded)\n"
            )

    return all_submissions


annie_render_679554 = (
    "299650: Introduction (graded)\n"
    "553716: Basic Addition (graded)\n"
    "805499: Basic Subtraction (graded)\n"
    "749969: Basic Multiplication (graded)\n"
    "763866: Basic Division (graded)\n"
    "979025: Midterm 1 (graded)\n"
    "870878: Logarithms (graded)\n"
    "126393: Antiderivatives (graded)\n"
    "122494: Actual Sorcery (graded)\n"
    "683132: Final Exam (graded)\n"
)

jeff_render_386814 = (
    "806809: HOMEWORK 1 (graded)\n"
    "212220: HOMEWORK 2 (graded)\n"
    "24048: HOMEWORK 3 (graded)\n"
    "982248: HOMEWORK 4 (graded)\n"
    "269027: HOMEWORK 5 - COPY 1 (graded)\n"
    "476501: HOMEWORK 7 (graded)\n"
    "654144: HOMEWORK 8 FINAL (graded)\n"
)


assert_equal(render_all("annie", 679554), annie_render_679554)
assert_equal(render_all("jeff", 386814), jeff_render_386814)


def plot_scores(user_token: str, course_id: int):
    """
    Creates a graph representing the distribution of the fractional scores in the course.
    Args:
        user_token (str): The user token of the user in question
        course_id (int): The course ID

    Returns:
        No return, but creates a distribution plot of the fractional scores of the course.
    """
    submissions = get_submissions(user_token, course_id)

    fractional_scores = []
    for submission in submissions:
        if submission.score and submission.assignment.points_possible != 0:
            fractional_scores.append(
                (submission.score / submission.assignment.points_possible) * 100
            )

    plt.hist(fractional_scores)
    plt.title("Fractional Scores")
    plt.ylabel("Total Points")
    plt.xlabel("Assignment Scores")
    plt.show()


# plot_scores('annie', 100167)
# plot_scores('abed', 100167)
# plot_scores('jeff', 100167)
