def make_operation(line):
    first_num, sign, second_num = line.split()
    first_num = float(first_num)
    second_num = int(second_num)
    result = 0
    if sign == '/':
        if second_num != 0:
            result = first_num / second_num
    elif sign == '*':
        result = first_num * second_num
    elif sign == '-':
        result = first_num - second_num
    elif sign == '+':
        result = first_num + second_num
    elif sign == '^':
        result = first_num ** second_num
    return f'{result:.2f}'
