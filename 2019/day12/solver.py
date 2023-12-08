if __name__ == "__main__":
    positions = open("input.txt").read().strip().split("\n")
    moons = []
    for pos in positions:
        x = int(pos.split("x=")[1].split(",")[0])
        y = int(pos.split("y=")[1].split(",")[0])
        z = int(pos.split("z=")[1].split(">")[0])
        moons.append(([x, y, z], [0, 0, 0]))
    for t in range(1000):
        for moon in moons:
            for other in moons:
                if other == moon:
                    continue
                for i in range(3):
                    if moon[0][i] > other[0][i]:
                        moon[1][i] -= 1
                    elif moon[0][i] < other[0][i]:
                        moon[1][i] += 1
        for moon in moons:
            for i in range(3):
                moon[0][i] += moon[1][i]
    res = 0
    for moon in moons:
        pos = sum(abs(i) for i in moon[0])
        vel = sum(abs(i) for i in moon[1])
        res += pos*vel
    print(res)

