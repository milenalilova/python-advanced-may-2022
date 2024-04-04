def cookbook(*args):
    cook_dict = {}
    for el in args:
        recipe_name, cuisine, ingredients = el
        if cuisine not in cook_dict.keys():
            cook_dict[cuisine] = {}
        if recipe_name not in cook_dict[cuisine]:
            cook_dict[cuisine][recipe_name] = []
        cook_dict[cuisine][recipe_name] = ingredients

    cook_dict = dict(sorted(cook_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ''

    for cuisine, recipes in cook_dict.items():
        recipes = dict(sorted(recipes.items()))
        output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe, ingr in recipes.items():
            output += f"  * {recipe} -> Ingredients: {', '.join(ingr)}\n"

    return output


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print()
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
))
print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
