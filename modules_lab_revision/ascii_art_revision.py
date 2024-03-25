from pyfiglet import figlet_format


def print_art(line):
    ascii_art = figlet_format(line)
    print(ascii_art)


current_line = input()
print_art(current_line)

# Variant 2 (simple)
# line = input()
# print(figlet_format(line))
