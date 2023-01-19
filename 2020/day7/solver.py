from collections import defaultdict

if __name__ == "__main__":
    bags = open("input.txt").read().strip().split("\n")
    container_dict = defaultdict(list)
    outmost_bags = set()
    for bag in bags:
        if "no other" in bag:
            continue
        parent_bag, child_bags = bag.replace("bags", "bag").split(" contain ")
        outmost_bags.add(parent_bag)
        for child_bag in child_bags[:-1].split(", "):
            container_dict[child_bag.split(" ", 1)[1]].append(parent_bag)

    gold_bags = 0
    visited = set()
    queue = ["shiny gold bag"]
    while queue:
        current = queue.pop()
        visited.add(current)
        for parent in container_dict[current]:
            if parent in visited or parent in queue:
                continue
            if parent in outmost_bags:
                gold_bags += 1
            queue.append(parent)
    print(gold_bags)

