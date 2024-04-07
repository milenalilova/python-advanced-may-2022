from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    rotations_dict = {}
    for rot in range(k + 1):
        sum_nums = 0
        for i in range(len(numbers)):
            sum_nums += numbers[i] * i
        rotations_dict[rot] = sum_nums
        el = numbers.pop()
        numbers.appendleft(el)

    best_rotation = max(rotations_dict, key=rotations_dict.get)
    return f"Best pureness {rotations_dict[best_rotation]} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
