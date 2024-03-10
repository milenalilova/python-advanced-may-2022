from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]
wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity[0]
    current_bottle = bottles_capacity[-1]

    if current_cup <= current_bottle:
        current_bottle -= current_cup
        wasted_water += current_bottle
        cups_capacity.popleft()
        bottles_capacity.pop()
    else:
        cups_capacity[0] -= current_bottle
        bottles_capacity.pop()

if not cups_capacity:

    bottles_left = []
    while bottles_capacity:
        bottles_left.append(str(bottles_capacity.pop()))
        print(f"Bottles: {' '.join(bottles_left)}")

else:
    cups_left = []
    while cups_capacity:
        cups_left.append(str(cups_capacity.popleft()))
    print(f"Cups: {' '.join(cups_left)}")

print(f"Wasted litters of water: {wasted_water}")
