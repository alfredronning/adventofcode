from math import lcm

def find_z_period(map, steps, current):
    i = 0
    while True:
        current = map[current][0 if steps[i%len(steps)] == "L" else 1]
        i += 1
        if current[-1] == "Z":
            return i


if __name__ == "__main__":
    steps, map = open("input.txt").read().strip().split("\n\n")
    map = dict((i.split(" = ")[0], i.split(" = ")[1][1:-1].split(", ")) for i in map.split("\n"))

    periods = []
    for key in map:
        if key[-1] == "A":
            periods.append(find_z_period(map, steps, key))
    print(lcm(*periods))

