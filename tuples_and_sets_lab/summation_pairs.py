numbers = [int(x) for x in input().split()]

target = int(input())
unique_combinations = set()
iterations = 0
for i1 in range(len(numbers)):
    for i2 in range(i1 + 1, len(numbers)):
        p1 = numbers[i1]
        p2 = numbers[i2]
        iterations += 1
        if p1 + p2 == target:
            print(f'{p1} + {p2} = {target}')
            unique_combinations.add((p1, p2))

print(f'Iterations done: {iterations}')
for combination in unique_combinations:
    print(combination)


# The smarter version. Given at Google interview
# numbers = [int(x) for x in input().split()]
#
# target = int(input())
# targets = set()
# values_map = {}
#
# for value in numbers:
#     if value in targets:
#         p1 = value
#         p2 = values_map[value]
#         print(f'{p1} + {p2} = {target}')
#     else:
#         targets.add(target - value)
#         values_map[target - value] = value
