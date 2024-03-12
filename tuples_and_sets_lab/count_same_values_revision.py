numbers = [float(x) for x in input().split(' ')]
occurrences_dict = {}

for num in numbers:
    if num not in occurrences_dict.keys():
        occurrences_dict[num] = 0
    occurrences_dict[num] += 1

for num, count in occurrences_dict.items():
    print(f"{num} - {count} times")
