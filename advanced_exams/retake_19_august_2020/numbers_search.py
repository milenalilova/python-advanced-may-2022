def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    duplicates = []
    missing_num = None
    for n in range(min_num, max_num + 1):
        if n not in args:
            missing_num = n
        if args.count(n) > 1 and n not in duplicates:
            duplicates.append(n)
        duplicates = sorted(duplicates)

    return [missing_num, duplicates]




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
