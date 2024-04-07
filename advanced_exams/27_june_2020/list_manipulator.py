def list_manipulator(nums_list, command, place, *args):
    if command == 'add':
        if place == 'beginning':
            if args:
                nums_list = list(args) + nums_list

        elif place == 'end':
            if args:
                nums_list = nums_list + list(args)

    elif command == 'remove':
        if place == 'beginning':
            if args:
                num = int(args[0])
                for i in range(num):
                    nums_list.remove(nums_list[0])
            else:
                nums_list.remove(nums_list[0])

        elif place == 'end':
            if args:
                num = int(args[0])
                for i in range(num):
                    nums_list.remove(nums_list[-1])
            else:
                nums_list.remove(nums_list[-1])

    return nums_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
