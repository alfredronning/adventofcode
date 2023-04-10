from random import shuffle

def replace_all(replacement_list, end_molecule, start_molecule):
    changed = True
    count = 0
    while changed:
        changed = False
        for fr, to in replacement_list:
            if to in end_molecule:
                changed = True
                count += end_molecule.count(to)
                end_molecule = end_molecule.replace(to, fr)
        if end_molecule == start_molecule:
            return count

if __name__ == "__main__":
    replacements, end_molecule = open("input.txt").read().strip().split("\n\n")
    start_molecule = "e"
    replacement_list = []
    for replacement in replacements.split("\n"):
        replacement_list.append(replacement.split(" => "))
    while True:
        shuffle(replacement_list)
        count = replace_all(replacement_list, end_molecule, start_molecule)
        if count is not None:
            print(count)
            break

