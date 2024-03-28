from collections import deque

times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

ducky_type_dict = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times and tasks:
    current_time = times.popleft()
    current_task = tasks.pop()
    product = current_time * current_task

    if 0 <= product <= 60:
        ducky_type_dict['Darth Vader Ducky'] += 1

    elif 61 <= product <= 120:
        ducky_type_dict['Thor Ducky'] += 1

    elif 121 <= product <= 180:
        ducky_type_dict['Big Blue Rubber Ducky'] += 1

    elif 181 <= product <= 240:
        ducky_type_dict['Small Yellow Rubber Ducky'] += 1

    elif product > 240:
        current_task -= 2
        tasks.append(current_task)
        times.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in ducky_type_dict.items():
    print(f"{duck}: {count}")
