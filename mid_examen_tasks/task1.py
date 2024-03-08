from collections import deque

eggs_sizes = deque([int(x) for x in input().split(', ')])
paper_sizes = deque([int(x) for x in input().split(', ')])

box_size = 50

filled_boxes = 0

while eggs_sizes and paper_sizes:
    egg = eggs_sizes[0]
    paper = paper_sizes[-1]

    if egg == 13:
        eggs_sizes.popleft()
        first_paper = paper_sizes.popleft()
        last_paper = paper_sizes.pop()
        paper_sizes.append(first_paper)
        paper_sizes.appendleft(last_paper)
        continue

    if egg <= 0:
        eggs_sizes.popleft()
        continue

    result = egg + paper

    if result <= box_size:
        eggs_sizes.popleft()
        paper_sizes.pop()
        filled_boxes += 1
    else:
        eggs_sizes.popleft()
        paper_sizes.pop()

if filled_boxes:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f'Eggs left: {", ".join([str(x) for x in eggs_sizes])}')

if paper_sizes:
    print(f'Pieces of paper left: {", ".join([str(x) for x in paper_sizes])}')


