def shopping_cart(*args):
    max_len_dict = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    meals_dict = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    for arg in args:
        if arg == 'Stop':
            break
        meal, product = arg
        if max_len_dict[meal] > len(meals_dict[meal]):
            if product not in meals_dict[meal]:
                meals_dict[meal].append(product)

    sorted_dict = dict(sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for value in meals_dict.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    output = ''

    for k, v in sorted_dict.items():
        output += f"{k}:\n"
        if v:
            for el in sorted(v):
                output += f" - {el}\n"

    return output


# Author's solution
# def shopping_cart(*args):
#     cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
#     for tuple_ in args:
#         meal = tuple_[0]
#         product = tuple_[1]
#         if tuple_ == 'Stop':
#             break
#         if meal == 'Pizza' and len(cart['Pizza']) == 4:
#             continue
#         elif meal == 'Soup' and len(cart['Soup']) == 3:
#             continue
#         elif meal == 'Dessert' and len(cart['Dessert']) == 2:
#             continue
#         if product not in cart[meal]:
#             cart[meal].append(product)
#
#     for value in cart.values():
#         if len(value) > 0:
#             break
#     else:
#         return 'No products in the cart!'
#
#     sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
#     result = ''
#     for tuple_ in sorted_cart:
#         result += f"{tuple_[0]}:\n"
#         sorted_product = sorted(tuple_[1])
#         for product in sorted_product:
#             result += f" - {product}\n"
#
#     return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
