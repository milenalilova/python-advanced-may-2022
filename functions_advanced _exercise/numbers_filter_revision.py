def even_odd_filter(**kwargs):
    result = {}
    for key, nums in kwargs.items():
        if key == 'odd':
            result[key] = [int(num) for num in nums if num % 2 != 0]
        elif key == 'even':
            result[key] = [int(num) for num in nums if num % 2 == 0]

    return dict(sorted(result.items(), key=lambda x: -len(x[-1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
