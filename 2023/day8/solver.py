if __name__ == "__main__":
    steps, map = open("input.txt").read().strip().split("\n\n")
    map = dict((i.split(" = ")[0], i.split(" = ")[1][1:-1].split(", ")) for i in map.split("\n"))
    i = 0
    current = "AAA"
    while True:
        current = map[current][0 if steps[i%len(steps)] == "L" else 1]
        i += 1
        if current == "ZZZ":
            break
    print(i)

