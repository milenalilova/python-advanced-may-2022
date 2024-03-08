from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

firework_types = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
is_firework_show = False

while firework_effects and explosive_power:
    firework = firework_effects[0]
    explosive = explosive_power[-1]
    result = firework + explosive

    if firework <= 0:
        firework_effects.popleft()
        continue
    if explosive <= 0:
        explosive_power.pop()
        continue
    if firework <= 0 and explosive <= 0:
        firework_effects.popleft()
        explosive_power.pop()
        continue

    if result % 3 == 0 and result % 5 != 0:
        firework_types['Palm Fireworks'] += 1
        firework = firework_effects.popleft()
        explosive = explosive_power.pop()

    elif result % 3 != 0 and result % 5 == 0:
        firework_types['Willow Fireworks'] += 1
        firework = firework_effects.popleft()
        explosive = explosive_power.pop()

    elif result % 3 == 0 and result % 5 == 0:
        firework_types['Crossette Fireworks'] += 1
        firework = firework_effects.popleft()
        explosive = explosive_power.pop()

    else:
        firework = firework_effects.popleft() - 1
        firework_effects.append(firework)
        continue

    if firework_types['Palm Fireworks'] >= 3 \
            and firework_types['Willow Fireworks'] >= 3 \
            and firework_types['Crossette Fireworks'] >= 3:
        is_firework_show = True
        break

if is_firework_show:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in firework_effects])}')

if explosive_power:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_power)}')

for key, value in firework_types.items():
    print(f'{key}: {value}')
