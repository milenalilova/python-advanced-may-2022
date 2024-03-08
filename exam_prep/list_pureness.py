# Pastebin


import sys
from collections import deque


def best_list_pureness(a_list, number):
    queue = deque(a_list)
    counter = 0
    best_pureness = -sys.maxsize
    rotation = 0

    while counter <= number:

        all_sum = 0
        for index, num in enumerate(queue):
            all_sum += index * num

        if all_sum > best_pureness:
            best_pureness = all_sum
            rotation = counter

        last = queue.pop()
        queue.appendleft(last)
        counter += 1

    return f"Best pureness {best_pureness} after {rotation} rotations"