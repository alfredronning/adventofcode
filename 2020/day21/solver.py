if __name__ == "__main__":
    rows = open("input.txt").read().strip().split("\n")
    possible_alergens = dict()
    for row in rows:
        ingredients, alergens = row[:-1].split(" (contains ")
        for alergen in alergens.split(", "):
            if alergen not in possible_alergens:
                possible_alergens[alergen] = ingredients.split()
            else:
                new = ingredients.split()
                old = possible_alergens[alergen]
                possible_alergens[alergen] = [alergen for alergen in old if alergen in new]
    alergen_ingredients = set()
    for ingredients in possible_alergens.values():
        for ingredient in ingredients:
            alergen_ingredients.add(ingredient)
    non_alergen_ingredient_count = 0
    for row in rows:
        for ingredient in row.split(" (contains ")[0].split():
            if ingredient not in alergen_ingredients:
                non_alergen_ingredient_count += 1
    print(non_alergen_ingredient_count)

