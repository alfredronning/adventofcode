from collections import defaultdict
from math import ceil

def find_ores_per_fuel(reaction_map):
    ore_count = 0
    needed = [(1, "FUEL")]
    rest = defaultdict(int)
    while needed:
        amount, elem = needed.pop()
        if elem == "ORE":
            ore_count += amount
            continue
        if rest[elem] > 0:
            if rest[elem] >= amount:
                rest[elem] -= amount
                continue
            else:
                amount -= rest[elem]
                rest[elem] = 0
        out_amount, inputs = reaction_map[elem]
        created_amount = ceil(amount/out_amount)*out_amount
        rest[elem] += created_amount-amount
        for inp_needed, inp_elem in inputs:
            needed.append((created_amount//out_amount*inp_needed, inp_elem))
    return ore_count

if __name__ == "__main__":
    reactions = open("input.txt").read().strip().split("\n")
    reaction_map = dict()
    for reaction in reactions:
        inps, out = reaction.split(" => ")
        out_count, out_elem = out.split()
        needed = []
        for inp in inps.split(", "):
            inp_count, inp_elem = inp.split()
            needed.append((int(inp_count), inp_elem))
        reaction_map[out_elem] = (int(out_count), needed)
    print(find_ores_per_fuel(reaction_map))

