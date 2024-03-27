from collections import deque

fuel = [int(x) for x in input().split()]
consumption_indexes = deque([int(x) for x in input().split()])
quantities = deque([int(x) for x in input().split()])

altitudes_reached = []
altitude = 1

for altitude in range(4):
    current_fuel = fuel.pop()
    current_index = consumption_indexes.popleft()
    current_quantity = quantities.popleft()

    difference = current_fuel - current_index

    if difference >= current_quantity:
        altitudes_reached.append(f"Altitude {altitude + 1}")
        print(f"John has reached: Altitude {altitude + 1}")
    else:
        fuel.append(current_fuel)
        consumption_indexes.appendleft(current_index)
        quantities.appendleft(current_quantity)
        print(f"John did not reach: Altitude {altitude + 1}")
        break
    altitude += 1

else:
    print("John has reached all the altitudes and managed to reach the top!")

if fuel:
    print("John failed to reach the top.")

    if altitudes_reached:
        print(f"Reached altitudes: {', '.join(altitudes_reached)}")
    else:
        print(f"John didn't reach any altitude.")
