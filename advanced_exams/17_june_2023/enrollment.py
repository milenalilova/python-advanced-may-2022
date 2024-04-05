def gather_credits(credits_needed, *args):
    gathered_credits = 0
    enrolled_courses = []
    for course_name, course_credits in args:
        if gathered_credits >= credits_needed:
            break
        if course_name not in enrolled_courses:
            enrolled_courses.append(course_name)
            gathered_credits += course_credits
    enrolled_courses = sorted(enrolled_courses)
    if gathered_credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses)}\n"

    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
