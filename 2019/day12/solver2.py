from math import lcm

def find_repeating_period(moons):
    visited = set()
    visited.add(moons)
    t = 0
    while True:
        new_moons = [list(m) for m in moons]
        for moon in new_moons:
            for other in new_moons:
                if other == moon:
                    continue
                if moon[0] > other[0]:
                    moon[1] -= 1
                elif moon[0] < other[0]:
                    moon[1] += 1
            
        for moon in new_moons:
            moon[0] += moon[1]
        moons = tuple(tuple(m) for m in new_moons)
        if moons in visited:
            return t+1
        visited.add(moons)
        t += 1

if __name__ == "__main__":
    positions = open("input.txt").read().strip().split("\n")
    moons_x = []
    moons_y = []
    moons_z = []
    for pos in positions:
        x = int(pos.split("x=")[1].split(",")[0])
        y = int(pos.split("y=")[1].split(",")[0])
        z = int(pos.split("z=")[1].split(">")[0])
        moons_x.append((int(x), 0))
        moons_y.append((int(y), 0))
        moons_z.append((int(z), 0))
    moons_x = tuple(moons_x)
    moons_y = tuple(moons_y)
    moons_z = tuple(moons_z)
    repeating_x = find_repeating_period(moons_x)
    repeating_y = find_repeating_period(moons_y)
    repeating_z = find_repeating_period(moons_z)
    print(lcm(repeating_x, repeating_y, repeating_z))

