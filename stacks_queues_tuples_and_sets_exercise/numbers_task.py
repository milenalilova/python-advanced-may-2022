first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0]
    target_set = command_parts[1]
    command_set = set([int(x) for x in command_parts[2:]])

    if command == 'Add':
        if target_set == 'First':
            first_set = first_set.union(command_set)
        elif target_set == 'Second':
            second_set = second_set.union(command_set)

    elif command == 'Remove':
        if target_set == 'First':
            first_set = first_set.difference(command_set)
        elif target_set == 'Second':
            second_set = second_set.difference(command_set)

    elif command == 'Check':
        print(first_set.issubset(second_set)) or second_set.issubset(first_set)

        # is_subset = False
        # if first_set.issubset(second_set) or second_set.issubset(first_set):
        #     is_subset = True
        # print(is_subset)

first_set = sorted(first_set)
second_set = sorted(second_set)

print(*first_set, sep=', ')
print(*second_set, sep=', ')
