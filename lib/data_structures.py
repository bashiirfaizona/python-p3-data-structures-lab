spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest.append(food)
    return spiciest


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶" * food["heat_level"]  # Multiply the emoji
        print(f"{name} ({cuisine}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total // len(spicy_foods)  # Use // to get an integer result


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods