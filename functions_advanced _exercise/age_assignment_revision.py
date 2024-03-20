def age_assignment(*args, **kwargs):
    names = {}
    for letter, age in kwargs.items():
        for name in args:
            if name[0] == letter:
                names[name] = int(age)

    sorted_result = sorted(names.items())
    sorted_result = '\n'.join([f"{name} is {age} years old." for name, age in sorted_result])

    return sorted_result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
