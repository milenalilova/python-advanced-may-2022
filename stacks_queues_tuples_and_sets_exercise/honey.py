from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue

    if current_nectar == 0:
        continue

    operator = symbols.popleft()
    honey_made += abs(operations[operator](current_bee, current_nectar))

print(f'Total honey made: {honey_made}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')

if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')
