from collections import deque

males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])

matches = 0

while males and females:
    first_female = females[0]
    last_male = males[-1]

    if first_female <= 0:
        females.popleft()
        continue

    if last_male <= 0:
        males.pop()
        continue

    if first_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if last_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if first_female == last_male:
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f'Matches: {matches}')

if males:
    reversed_males = (", ".join([str(x) for x in reversed(males)]))
    print(f'Males left: {reversed_males}')
else:
    print('Males left: none')

if females:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print('Females left: none')
