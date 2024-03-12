numbers = [int(x) for x in input().split(' ')]
target_num = int(input())
iterations = 0
unique_pairs = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        iterations += 1
        num_one = numbers[i]
        num_two = numbers[j]

        if num_one + num_two == target_num:
            print(f"{num_one} + {num_two} = {target_num}")
            unique_pairs.add((num_one, num_two))

print(f"Iterations done: {iterations}")
[print(pair) for pair in unique_pairs]


