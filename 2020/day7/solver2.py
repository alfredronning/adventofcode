def rec_sumbags(container_dict, current_bag, amount):
    res = 0
    if current_bag in container_dict:
        for child_amount, child_bag in container_dict[current_bag]:
            res += rec_sumbags(container_dict, child_bag, child_amount)
    return (res+1)*amount

if __name__ == "__main__":
    bags = open("input.txt").read().strip().split("\n")
    container_dict = dict()
    for bag in bags:
        if "no other" in bag:
            continue
        parent_bag, child_bags = bag.replace("bags", "bag").split(" contain ")
        container_dict[parent_bag] = [(int(bag.split(" ", 1)[0]), bag.split(" ", 1)[1]) for bag in child_bags[:-1].split(", ")]
    print(rec_sumbags(container_dict, "shiny gold bag", 1)-1)

