from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

fireworks_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
is_perfect_show = False

while firework_effects and explosive_power and not is_perfect_show:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    if firework_effects[0] <= 0 and explosive_power[-1] <= 0:
        firework_effects.popleft()
        explosive_power.pop()
        continue

    current_firework = firework_effects.popleft()
    current_explosive = explosive_power.pop()

    sum_values = current_firework + current_explosive

    if sum_values % 15 == 0:
        fireworks_dict['Crossette Fireworks'] += 1

    elif sum_values % 5 == 0:
        fireworks_dict['Willow Fireworks'] += 1

    elif sum_values % 3 == 0:
        fireworks_dict['Palm Fireworks'] += 1

    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_explosive)
    if fireworks_dict['Palm Fireworks'] >= 3 and \
            fireworks_dict['Willow Fireworks'] >= 3 and \
            fireworks_dict['Crossette Fireworks'] >= 3:
        is_perfect_show = True

if is_perfect_show:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for k, v in fireworks_dict.items():
    print(f"{k}: {v}")
