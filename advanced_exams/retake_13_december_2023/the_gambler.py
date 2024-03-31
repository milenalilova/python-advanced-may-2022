def find_start_position(board, size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'G':
                return [i, j]


def find_next_position(command, position, board):
    row, col = position
    board[row][col] = '-'

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


def handle_next_position(position, amount, board):
    row, col = position

    if board[row][col] == 'W':
        amount += 100
    elif board[row][col] == 'P':
        amount -= 200
    elif board[row][col] == 'J':
        amount += 100000
    board[row][col] = 'G'
    return amount


def the_gambler():
    size = int(input())
    board = [list(input()) for _ in range(size)]
    current_position = find_start_position(board, size)

    initial_amount = 100

    command = input()
    while command != 'end':

        next_position = find_next_position(command, current_position, board)
        if not is_inside(next_position, size):
            print("Game over! You lost everything!")
            break
        initial_amount = handle_next_position(next_position, initial_amount, board)

        if initial_amount >= 100000:
            print(f"You win the Jackpot! End of the game. Total amount: {initial_amount}$")
            for row in board:
                print(*row, sep='')
            break
        if initial_amount <= 0:
            print("Game over! You lost everything!")
            break

        command = input()

    else:
        print(f"End of the game. Total amount: {initial_amount}$")
        for row in board:
            print(*row, sep='')


the_gambler()
