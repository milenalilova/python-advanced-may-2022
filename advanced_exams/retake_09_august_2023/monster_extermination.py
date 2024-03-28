from collections import deque

monsters_armor_values = deque([int(x) for x in input().split(',')])
soldiers_impact_values = [int(x) for x in input().split(',')]

monsters_killed = 0

while monsters_armor_values and soldiers_impact_values:
    current_armor = monsters_armor_values.popleft()
    current_impact = soldiers_impact_values.pop()

    if current_impact >= current_armor:
        diff = current_impact - current_armor
        monsters_killed += 1
        if soldiers_impact_values:
            soldiers_impact_values[-1] += diff
        else:
            if diff > 0:
                soldiers_impact_values.append(diff)
    else:
        diff = current_armor - current_impact
        monsters_armor_values.append(diff)

if not monsters_armor_values:
    print("All monsters have been killed!")

if not soldiers_impact_values:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
