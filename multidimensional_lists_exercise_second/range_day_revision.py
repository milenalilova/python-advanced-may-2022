def find_next_position(row, col, direction, steps):
    if direction == 'right':
        return row, col + steps
    elif direction == 'left':
        return row, col - steps
    elif direction == 'up':
        return row - steps, col
    elif direction == 'down':
        return row + steps, col


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


shotgun_range = [[ch for ch in input().split()] for ch in range(5)]

shooter_row = 0
shooter_col = 0

targets = 0
targets_hit = []

for row in range(5):
    for col in range(5):
        if shotgun_range[row][col] == 'A':
            shooter_row = row
            shooter_col = col
        elif shotgun_range[row][col] == 'x':
            targets += 1

shotgun_range[shooter_row][shooter_col] = '.'

n = int(input())

for _ in range(n):
    command = input().split()
    instruction, direction = command[0], command[1]

    if instruction == 'move':
        steps = int(command[2])
        next_row, next_col = find_next_position(shooter_row, shooter_col, direction, steps)

        if is_inside(next_row, next_col, 5) and shotgun_range[next_row][next_col] == '.':
            shooter_row, shooter_col = next_row, next_col

    elif instruction == 'shoot':
        target_row, target_col = find_next_position(shooter_row, shooter_col, direction, 1)
        while is_inside(target_row, target_col, 5):
            if shotgun_range[target_row][target_col] == 'x':
                targets -= 1
                shotgun_range[target_row][target_col] = '.'
                targets_hit.append([target_row, target_col])
                break
            target_row, target_col = find_next_position(target_row, target_col, direction, 1)

        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

for row in targets_hit:
    print(row, sep='\n')

