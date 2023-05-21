from pprint import pprint

with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        count = int(file.readline())
        name = []
        for i in range(count):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            ingr = dict(ingredient_name=ingredient_name, quantity=int(quantity), measure=measure)
            name.append(ingr)
        file.readline()
        cook_book[dish] = name
    # pprint(cook_book, sort_dicts=False)
def get_ingredients(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for item in cook_book[dish]:
            quantity = item['quantity']
            if item['ingredient_name'] not in ingredients:
                ingredients[item['ingredient_name']] = {'measure': item['measure'], 'quantity': quantity * person_count}
            else:
                ingredients[item['ingredient_name']]['quantity'] += quantity * person_count
    return ingredients

selected_dishes = ['Омлет', 'Запеченный картофель']
person_count = 2
ingredients = get_ingredients(selected_dishes, person_count)

pprint(ingredients)