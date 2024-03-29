from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

is_pouched_filled = False

bombs_dict = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
while bomb_effects and bomb_casings and not is_pouched_filled:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    sum_values = current_effect + current_casing

    if sum_values == 40:
        bombs_dict['Datura Bombs'] += 1

    elif sum_values == 60:
        bombs_dict['Cherry Bombs'] += 1

    elif sum_values == 120:
        bombs_dict['Smoke Decoy Bombs'] += 1

    else:
        current_casing -= 5
        bomb_casings.append(current_casing)
        bomb_effects.appendleft(current_effect)

    if bombs_dict['Datura Bombs'] >= 3 and bombs_dict['Cherry Bombs'] >= 3 and bombs_dict['Smoke Decoy Bombs'] >= 3:
        is_pouched_filled = True

if is_pouched_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

sorted_dict = dict(sorted(bombs_dict.items()))

for k, v in sorted_dict.items():
    print(f"{k}: {v}")
