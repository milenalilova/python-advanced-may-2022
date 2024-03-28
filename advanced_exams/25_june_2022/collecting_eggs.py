from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])

boxes_field = 0

while eggs and papers:
    first_egg = eggs[0]

    if first_egg <= 0:
        eggs.popleft()
    elif first_egg == 13:
        eggs.popleft()
        first_paper = papers.popleft()
        last_paper = papers.pop()
        papers.append(first_paper)
        papers.appendleft(last_paper)
    else:
        first_egg = eggs.popleft()
        last_paper = papers.pop()

        if first_egg + last_paper <= 50:
            boxes_field += 1

if boxes_field:
    print(f"Great! You filled {boxes_field} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
