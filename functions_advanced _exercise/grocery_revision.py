def grocery_store(**kwargs):
    products = {}
    for product, quantity in kwargs.items():
        products[product] = (int(quantity))

    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    sorted_products = '\n'.join([f"{product}: {quantity}" for product, quantity in products])

    return sorted_products


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
