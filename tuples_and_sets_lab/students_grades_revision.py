students_count = int(input())
students_dict = {}

for i in range(students_count):
    student_info = input().split(' ')
    name = student_info[0]
    grade = float(student_info[1])

    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(grade)

for name, grade in students_dict.items():
    average = sum(grade) / len(grade)
    grade_str = ' '.join(f"{grade:.2f}" for grade in grade)

    print(f"{name} -> {grade_str} (avg: {average:.2f})")
