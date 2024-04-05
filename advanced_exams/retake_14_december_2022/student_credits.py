def students_credits(*args):
    credits_earned = 0
    courses_dict = {}
    for arg in args:
        course_name, credits, max_test_points, students_points = str(arg).split('-')
        proportion = int(students_points) / int(max_test_points)
        current_credits_earned = int(credits) * proportion
        credits_earned += current_credits_earned
        courses_dict[course_name] = current_credits_earned

    sorted_courses_dict = dict(sorted(courses_dict.items(), key=lambda x: -x[1]))
    output = ''
    printed_dict = ''

    for k, v in sorted_courses_dict.items():
        printed_dict += f"{k} - {v:.1f}\n"

    if credits_earned >= 240:
        output += f"Diyan gets a diploma with {credits_earned:.1f} credits.\n"
        output += printed_dict
        return output
    else:
        output = f"Diyan needs {240 - credits_earned:.1f} credits more for a diploma.\n"
        output += printed_dict
        return output


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
