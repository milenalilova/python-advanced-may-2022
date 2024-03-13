first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    command = input().split()
    instruction = command[0]
    sequence_name = command[1]
    nums = set(int(x) for x in command[2:])

    if instruction == 'Add':
        if sequence_name == 'First':
            for num in nums:
                first_sequence.add(num)

        elif sequence_name == 'Second':
            for num in nums:
                second_sequence.add(num)

    elif instruction == 'Remove':
        if sequence_name == 'First':
            for num in nums:
                if num in first_sequence:
                    first_sequence.remove(num)
        elif sequence_name == 'Second':
            for num in nums:
                if num in second_sequence:
                    second_sequence.remove(num)

    elif instruction == 'Check':
        is_subset = False
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            is_subset = True
        print(is_subset)

first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(*first_sequence, sep=', ')
print(*second_sequence, sep=', ')
