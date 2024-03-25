def print_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print(j + 1, end=' ')
        print()

    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            print(j + 1, end=' ')
        print()