if __name__ == "__main__":
    boxes = open("input.txt").read().strip().split("\n")
    twos = 0
    trees = 0
    for box in boxes:
        if any(box.count(c) == 2 for c in set(box)):
            twos += 1
        if any(box.count(c) == 3 for c in set(box)):
            trees += 1
    print(twos*trees)

