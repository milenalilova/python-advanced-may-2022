def find_initial_position(area, size):
    for i in range(size):
        for j in range(size):
            if area[i][j] == 'S':
                return [i, j]


def find_next_position(command, position, area):
    row, col = position
    area[row][col] = '-'

    if command == 'up':
        position[0] -= 1
    elif command == 'down':
        position[0] += 1
    elif command == 'left':
        position[1] -= 1
    elif command == 'right':
        position[1] += 1

    return position


def is_inside(position, size):
    row, col = position
    if not 0 <= row < size or not 0 <= col < size:
        return False
    return True


def adjust_position_inside(command, position, area, size):
    row, col = position
    # area[row][col] = '-'

    if command == 'up':
        position[0] = size - 1
    elif command == 'down':
        position[0] = 0
    elif command == 'left':
        position[1] = size - 1
    elif command == 'right':
        position[1] = 0

    return position


def handle_next_position(position, area, amount, condition):
    current_char = area[position[0]][position[1]]
    condition = False

    if current_char == 'W':
        amount = 0
        condition = True
    elif current_char == '-':
        pass
    else:
        amount += int(current_char)

    area[position[0]][position[1]] = 'S'
    return amount, condition


size = int(input())
fishing_area = [list(input()) for _ in range(size)]
catch_amount = 0
lost_catch = False
is_successful_season = False

current_position = find_initial_position(fishing_area, size)
last_position = []

command = input()

while command != 'collect the nets':

    next_position = find_next_position(command, current_position, fishing_area)
    if not is_inside(next_position, size):
        next_position = adjust_position_inside(command, next_position, fishing_area, size)
    catch_amount, lost_catch = handle_next_position(next_position, fishing_area, catch_amount, lost_catch)
    if catch_amount >= 20:
        is_successful_season = True
    if lost_catch:
        last_position = current_position
        break

    command = input()

if lost_catch:
    print(
        f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join(map(str, last_position))}]")
else:
    if is_successful_season:
        print("Success! You managed to reach the quota!")
    else:
        print(
            f"You didn't catch enough fish and didn't reach the quota! You need {20 - catch_amount} tons of fish more.")

    if catch_amount > 0:
        print(f"Amount of fish caught: {catch_amount} tons.")
    for row in fishing_area:
        print(*row, sep='')
