def shopping_list(budget, **kwargs):
    bought_products = {}

    if budget < 100:
        return f"You do not have enough budget."

    for product, info in kwargs.items():
        price, quantity = info
        if budget >= price * quantity:
            bought_products[product] = price * quantity
            budget -= price * quantity
            if len(bought_products) >= 5:
                break

    output = ''
    for product, price in bought_products.items():
        output += f"You bought {product} for {price:.2f} leva.\n"

    return output.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
