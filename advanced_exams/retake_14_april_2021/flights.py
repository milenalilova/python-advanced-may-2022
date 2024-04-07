from collections import deque


def flights(*args):
    destinations_deque = deque(args)
    destinations_dict = {}

    while True:
        if destinations_deque[0] == 'Finish':
            return destinations_dict
        destination = destinations_deque.popleft()
        passengers = destinations_deque.popleft()
        if destination not in destinations_dict:
            destinations_dict[destination] = 0
        destinations_dict[destination] += passengers

    return destinations_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
