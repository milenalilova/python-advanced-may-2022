def rectangle(length, width):
    # functions always on top

    def area():
        return length * width

    def perimeter():
        return 2 * length + 2 * width

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
