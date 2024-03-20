def concatenate(*args, **kwargs):
    concat_string = ''
    for string in args:
        concat_string += string

    for key, value in kwargs.items():
        while key in concat_string:
            concat_string=concat_string.replace(key, value)

    return concat_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
