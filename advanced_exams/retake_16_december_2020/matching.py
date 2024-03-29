from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    current_female = females[0]
    current_male = males[-1]

    if current_female <= 0:
        females.popleft()
        continue

    if current_male <= 0:
        males.pop()
        continue

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_female == current_male:
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
