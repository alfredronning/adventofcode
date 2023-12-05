def get_val(map, value):
    for dest, source, r in map:
        if value >= source and value < source + r:
            return value - source + dest
    return value

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n\n")
    seeds = [int(i) for i in inp[0].split(": ")[1].split()]
    maps = [[], [], [], [], [], [], []]
    for i in range(len(maps)):
        rows = inp[i+1].split("\n")[1:]
        for row in rows:
            maps[i].append(tuple([int(k) for k in row.split()]))

    for m in range(len(maps)):
        for i in range(len(seeds)):
            seeds[i] = get_val(maps[m], seeds[i])
    print(min(seeds))

