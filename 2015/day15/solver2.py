import re

PROPERTIES_COUNT = 5

def add_ingredient(current_properties, properties, count):
    return [current_properties[i]*count+properties[i] for i in range(PROPERTIES_COUNT)]

def calc_res(properties):
    if properties[-1] != 500:
        return 0
    res = 1
    for p in properties[:-1]:
        res *= max(p, 0)
    return res

def find_best_combo(ingredient_dict, current_ingredient, remainding, properties, visited):
    next_ingredients = [i for i in ingredient_dict.keys() if i not in visited]
    current_properties = ingredient_dict[current_ingredient]
    if not remainding:
        return calc_res(properties)
    if not len(next_ingredients):
        properties = add_ingredient(current_properties, properties, remainding)
        return calc_res(properties)

    next_ingredient = next_ingredients[0]
    visited = visited+[next_ingredient]
    res = 0
    for usage in range(remainding+1):
        next_properties = add_ingredient(current_properties, properties, usage)
        current_res = find_best_combo(ingredient_dict, next_ingredient, remainding-usage, next_properties, visited)
        res = max(res, current_res)
    return res

if __name__ == "__main__":
    ingredients = open("input.txt").read().strip().split("\n")
    ingredient_dict = dict()
    for ingredient in ingredients:
        groups = re.search("(.*):.* (-?\d*), .* (-?\d*).*, .* (-?\d*).*, .* (-?\d*).*, .* (-?\d*).*", ingredient)
        ingredient_dict[groups.group(1)] = [int(groups.group(i+2)) for i in range(PROPERTIES_COUNT)]
    visited = []
    current = list(ingredient_dict.keys())[0]
    res = find_best_combo(ingredient_dict, current, 100, [0]*PROPERTIES_COUNT, visited+[current])
    print(res)


