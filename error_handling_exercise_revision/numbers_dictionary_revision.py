#  Completed code

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)

numbers_dictionary = {}

line = input()

# Provided code

# while line != "
# ":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
#
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)