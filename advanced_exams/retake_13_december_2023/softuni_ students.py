def softuni_students(*args, **kwargs):
    course_dict = {}

    for data in args:
        course_id, username = data
        if username not in course_dict:
            course_dict[username] = {}
        if course_id not in course_dict[username]:
            course_dict[username][course_id] = None

    for course_id, course_name in kwargs.items():
        for name, course_info in course_dict.items():
            for id, c_name in course_info.items():
                if course_id == id:
                    course_dict[name][id] = course_name

    invalid_students = []
    for k, v in course_dict.items():
        for k1, v1 in v.items():
            if v1 is None:
                invalid_students.append(k)
    for student in invalid_students:
        if student in course_dict.keys():
            del course_dict[student]

    result = ''

    course_dict = dict(sorted(course_dict.items()))
    for k, v in course_dict.items():
        for k1, v1 in v.items():
            result += f"*** A student with the username {k} has successfully finished the course {v1}!\n"

    if invalid_students:
        invalid_students = sorted(invalid_students)
        result += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return result



# Authors solution
# def softuni_students(*args, **kwargs):
#     course_dict = {}
#
#     for data in args:
#         course_id, username = data
#         if username not in course_dict:
#             course_dict[username] = {}
#         if course_id not in course_dict[username]:
#             course_dict[username][course_id] = None
#
#     for course_id, course_name in kwargs.items():
#         for name, course_info in course_dict.items():
#             for id, c_name in course_info.items():
#                 if course_id == id:
#                     course_dict[name][id] = course_name
#
#     invalid_students = []
#     for k, v in course_dict.items():
#         for k1, v1 in v.items():
#             if v1 is None:
#                 invalid_students.append(k)
#     for student in invalid_students:
#         if student in course_dict.keys():
#             del course_dict[student]
#
#     result = ''
#
#     course_dict = dict(sorted(course_dict.items()))
#     for k, v in course_dict.items():
#         for k1, v1 in v.items():
#             result += f"*** A student with the username {k} has successfully finished the course {v1}!\n"
#
#     if invalid_students:
#         invalid_students = sorted(invalid_students)
#         result += f"!!! Invalid course students: {', '.join(invalid_students)}"
#
#     return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
