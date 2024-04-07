def stock_availability(inventory_list, command, *args):
    new_inventory_list = inventory_list.copy()
    if command == 'delivery':
        for flavour in args:
            new_inventory_list.append(flavour)
    elif command == 'sell':
        if not args:
            new_inventory_list.remove(new_inventory_list[0])
        for arg in args:
            if type(arg) == str:
                if arg in new_inventory_list:
                    while arg in new_inventory_list:
                        new_inventory_list.remove(arg)

            elif type(arg) == int:
                if arg >= len(new_inventory_list):
                    new_inventory_list.clear()
                else:
                    for i in range(arg):
                        new_inventory_list.remove(new_inventory_list[0])

    return new_inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
