from collections import deque

names = input()
tosses = int(input())
kids = deque(names.split(' '))

counter = 0

while len(kids) > 1:
    counter += 1
    kid = kids.popleft()

    if counter < tosses:
        kids.append(kid)

    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {kids.popleft()}")
