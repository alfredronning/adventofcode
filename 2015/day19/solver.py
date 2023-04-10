if __name__ == "__main__":
    replacements, start_molecule = open("input.txt").read().strip().split("\n\n")
    replacement_dict = dict()
    outputs = set()
    for replacement in replacements.split("\n"):
        k, v = replacement.split(" => ")
        if k in replacement_dict:
            replacement_dict[k].append(v)
        else:
            replacement_dict[k] = [v]
    for i in range(len(start_molecule)):
        if start_molecule[i] in replacement_dict:
            for replacement in replacement_dict[start_molecule[i]]:
                outputs.add(start_molecule[:i]+replacement+start_molecule[i+1:])
        if start_molecule[i:i+2] in replacement_dict:
            for replacement in replacement_dict[start_molecule[i:i+2]]:
                outputs.add(start_molecule[:i]+replacement+start_molecule[i+2:])
    print(len(outputs))

