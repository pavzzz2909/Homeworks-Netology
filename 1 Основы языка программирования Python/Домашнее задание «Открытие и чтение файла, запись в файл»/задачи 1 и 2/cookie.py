from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipe in file:
        key = recipe.strip()
        count = int(file.readline().strip())
        ingredients_data = []
        for ingredients in range(count):
            ingredient_name, quantity, measure = file.readline().split(" | ")
            ingredients_data.append({'ingredient_name': ingredient_name,
                            'quantity': int(quantity),
                            'measure': measure.strip("\n")})
        cook_book[key] = ingredients_data
        file.readline()
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dishes = {}
    for dish in dishes:
        ingredient_quantity = 0
        for ingredients in cook_book[dish]:
            ingredient = ingredients['ingredient_name']
            ingredient_quantity = ingredients['quantity'] * person_count
            ingredient_measure = ingredients['measure']
            if ingredient not in ingredients_dishes:
                ingredients_dishes[ingredient] = {'measure':ingredient_measure,'quantity':ingredient_quantity}
            else:
                ingredients_dishes[ingredient]['quantity'] += ingredient_quantity
    return ingredients_dishes

pprint(get_shop_list_by_dishes(['‘ахитос', 'ќмлет'], 2))