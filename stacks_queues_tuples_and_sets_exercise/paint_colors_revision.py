from collections import deque

line = deque(input().split())
collected_colours = []

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

while line:

    left_word = line.popleft()
    right_word = line.pop() if line else ''

    word = left_word + right_word
    if word in main_colors or word in secondary_colors:
        collected_colours.append(word)
        continue

    word = right_word + left_word
    if word in main_colors or word in secondary_colors:
        collected_colours.append(word)
        continue

    left_word = left_word[:-1]
    right_word = right_word[:-1]

    if left_word:
        line.insert(len(line) // 2, left_word)

    if right_word:
        line.insert(len(line) // 2, right_word)

result = []

forming_colours = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for colour in collected_colours:
    if colour in main_colors:
        result.append(colour)
    else:
        is_collected = True
        for helper_colour in forming_colours[colour]:
            if helper_colour not in collected_colours:
                is_collected = False
                break
        if is_collected:
            result.append(colour)

print(result)

