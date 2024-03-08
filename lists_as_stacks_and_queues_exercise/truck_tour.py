from collections import deque

pumps_count = int(input())
petrol_pumps = deque()
for _ in range(pumps_count):
    petrol_pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    trunk = 0
    failed = False
    for petrol, distance in petrol_pumps:    #  for pump in petrol_pumps  pump = petrol, distance
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempt)
        break
