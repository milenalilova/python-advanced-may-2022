def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


size = int(input())
racing_number = input()

route = [list(input().split()) for _ in range(size)]

tunnels_coordinates = []
for i in range(size):
    for j in range(size):
        if route[i][j] == 'T':
            tunnels_coordinates.append([i, j])

car_row, car_col = 0, 0
km_covered = 0

while True:
    command = input()
    if command == 'End':
        route[car_row][car_col]='C'
        print(f"Racing car {racing_number} DNF.")
        print(f"Distance covered {km_covered} km.")
        break

    next_row, next_col = find_next_position(command, car_row, car_col)

    if [next_row, next_col] in tunnels_coordinates:
        tunnels_coordinates.remove([next_row, next_col])
        route[next_row][next_col] = '.'
        car_row, car_col = tunnels_coordinates[0][0], tunnels_coordinates[0][1]
        route[car_row][car_col] = '.'
        km_covered += 30

    elif route[next_row][next_col] == '.':
        car_row, car_col = next_row, next_col
        km_covered += 10

    elif route[next_row][next_col] == 'F':
        car_row, car_col = next_row, next_col
        route[car_row][car_col] = 'C'
        km_covered += 10
        print(f"Racing car {racing_number} finished the stage!")
        print(f"Distance covered {km_covered} km.")
        break

for row in route:
    print(*row, sep='')
