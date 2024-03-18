size = int(input())

field = [[ch for ch in input().split()] for ch in range(size)]

alice_row = 0
alice_col = 0

collected_tea_bags = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == 'A':
            alice_row = row
            alice_col = col

is_out = False

while collected_tea_bags < 10:
    field[alice_row][alice_col] = '*'

    direction = input()

    if direction == 'right':
        alice_col += 1

    elif direction == 'left':
        alice_col -= 1

    elif direction == 'up':
        alice_row -= 1

    elif direction == 'down':
        alice_row += 1

    if not 0 <= alice_row < size or not 0 <= alice_col < size:
        break

    if field[alice_row][alice_col] == 'R':
        field[alice_row][alice_col] = '*'
        break

    if field[alice_row][alice_col].isdigit():
        collected_tea_bags += int(field[alice_row][alice_col])
        field[alice_row][alice_col] = '*'

if collected_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in field:
    print(*row, sep=' ')
