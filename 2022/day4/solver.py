def fully_contained(elfs):
    first, second = elfs.split(",")
    first = int(first.split("-")[0]), int(first.split("-")[1])
    second = int(second.split("-")[0]), int(second.split("-")[1])
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    if first[0] <= second[0] and first[1] >= second[1]:
        return True
    return False

if __name__ == "__main__":
    pairs = open("input.txt").read().strip().split("\n")
    print(sum(fully_contained(pair) for pair in pairs))

