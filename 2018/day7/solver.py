from collections import defaultdict
if __name__ == "__main__":
    dependecies = open("input.txt").read().strip().split("\n")
    dep_dict = defaultdict(list)
    steps = set(dep_dict)
    for dependency in dependecies:
        ds = dependency.split()
        a, b = ds[1], ds[7]
        steps.add(a)
        steps.add(b)
        dep_dict[b].append(a)
    steps = sorted(list(steps))
    order = ""
    while steps:
        next_step = [s for s in steps if len([o for o in dep_dict[s] if o not in order]) == 0][0]
        steps.remove(next_step)
        order += next_step
    print(order)

