from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

bombs_made = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

is_bomb_pouch = False

while bomb_effects and bomb_casings:
    effect = bomb_effects[0]
    casing = bomb_casings[-1]
    result = effect + casing

    if result in bombs:
        key = bombs[result]
        bombs_made[key] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if bombs_made['Datura Bombs'] >= 3 and bombs_made['Cherry Bombs'] >= 3 and bombs_made['Smoke Decoy Bombs'] >= 3:
        is_bomb_pouch = True
        break

if is_bomb_pouch:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')
else:
    print(f'Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print('Bomb Casings: empty')

sorted_bombs = sorted(bombs_made.items(), key=lambda x: x[0])
for i in sorted_bombs:
    print(f'{i[0]}: {i[1]}')
