def avg(values):
    return sum(values) / len(values)


number = int(input())

student_record = {}

for i in range(number):
    student_info = tuple(input().split())
    name, grade = student_info
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(float(grade))

for name, grades in student_record.items():
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg = avg(grades)
    print(f'{name} -> {grades_formatted} (avg: {grades_avg:.2f})')
