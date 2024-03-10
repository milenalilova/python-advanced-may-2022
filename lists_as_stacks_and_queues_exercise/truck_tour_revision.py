from collections import deque

stations_count = int(input())

stations_circle = deque()

for _ in range(stations_count):
    stations_circle.append([int(x) for x in input().split(' ')])

for attempt in range(stations_count):
    trunk_amount = 0
    failed = False
    for petrol, distance in stations_circle:
        trunk_amount = trunk_amount + petrol - distance
        if trunk_amount < 0:
            failed = True
            break
    if failed:
        stations_circle.append(stations_circle.popleft())
    else:
        print(attempt)
        break
