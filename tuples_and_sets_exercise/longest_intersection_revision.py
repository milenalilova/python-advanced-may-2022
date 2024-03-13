n = int(input())

longest_intersection = set()

for _ in range(n):

    ranges = input().split('-')
    first_start, first_end = ranges[0].split(',')
    second_start, second_end = ranges[1].split(',')

    first_start, first_end = int(first_start), int(first_end)
    second_start, second_end = int(second_start), int(second_end)

    first_range = set(x for x in range(first_start, first_end + 1))
    second_range = set(x for x in range(second_start, second_end + 1))
    current_intersection = first_range.intersection(second_range)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

result = ', '.join(str(x) for x in longest_intersection)
print(f"Longest intersection is [{result}] with length {len(longest_intersection)}")
