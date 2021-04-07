def parse_input():
    num_recipes = int(input())
    recipes = {}
    for i in range(num_recipes):
        num_ingredients, real_portions, desired_portions = map(int, input().split())
        ingredients = []
        for _ in range(num_ingredients):
            name, raw_weight, raw_percentage = input().split()
            weight = float(raw_weight)
            percentage = float(raw_percentage)
            ingredients.append({
                'name' : name,
                'weight' : weight, 
                'percentage' : percentage})
        recipes[i + 1] = {
            'real-portions' : real_portions,
            'desired-portions': desired_portions,
            'ingredients' : ingredients
        }
    return recipes


def process_recipes(recipes):
    for key, recipe in recipes.items():
        print('Recipe # {}'.format(key))
        scaling_factor = recipe['desired-portions'] / recipe['real-portions']
        main_scaled_weight = 0.0
        for ingredient in recipe['ingredients']:
            if ingredient['percentage'] == 100.0:
                main_scaled_weight = ingredient['weight'] * scaling_factor
                break
        for ingredient in recipe['ingredients']:
            scaled_weight = (ingredient['percentage'] / 100) * main_scaled_weight
            print('{} {:0.1f}'.format(ingredient['name'], scaled_weight))
        print(40 * '-')


if __name__ == '__main__':
    recipes = parse_input()
    process_recipes(recipes)
