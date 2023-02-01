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
    # reduce all possibilites down to 1
    checked = set()
    while len(checked) < len(possible_alergens):
        for alergen in possible_alergens:
            if alergen in checked:
                continue
            if len(possible_alergens[alergen]) == 1:
                checked.add(alergen)
                only_choice = possible_alergens[alergen][0]
                for other_alergen in possible_alergens:
                    if other_alergen == alergen:
                        continue
                    if only_choice in possible_alergens[other_alergen]:
                        possible_alergens[other_alergen].remove(only_choice)
    print(",".join(possible_alergens[alergen][0] for alergen in sorted(possible_alergens.keys())))
