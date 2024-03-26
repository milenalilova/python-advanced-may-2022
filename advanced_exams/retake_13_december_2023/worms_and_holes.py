from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

initial_worms_count = len(worms)
initial_holes_count = len(holes)
matches = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_worm == current_hole:
        matches += 1
    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and initial_worms_count == matches:
    print("Every worm found a suitable hole!")
elif not worms and initial_worms_count != matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
