def naughty_or_nice_list(kids_names, *args, **kwargs):
    kids_dict = {'Nice': [],
                 'Naughty': [],
                 'Not found': []
                 }
    counting_numbers_dict = {

    }
    names_list = []
    for count_num, name in kids_names:
        names_list.append(name)
        if count_num not in counting_numbers_dict:
            counting_numbers_dict[count_num] = []
        counting_numbers_dict[count_num].append(name)

    if args:
        for arg in args:
            number, characteristic = arg.split('-')
            number = int(number)
            if number in counting_numbers_dict:
                if len(counting_numbers_dict[number]) == 1:
                    kids_dict[characteristic].append(counting_numbers_dict[number][0])
                    names_list.remove(counting_numbers_dict[number][0])
                else:
                    continue

    if kwargs:
        for name, characteristic in kwargs.items():
            if names_list.count(name) == 1:
                kids_dict[characteristic].append(name)
                if name in names_list:
                    names_list.remove(name)
            else:
                continue

    kids_dict['Not found'].extend(names_list)

    output = ''
    for k, v in kids_dict.items():
        if v:
            output += f"{k}: {', '.join(v)}\n"

    return output


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
