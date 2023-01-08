from collections import defaultdict

def find_covered(sensors, line):
    sensors_on_line = set()
    cant_be = defaultdict(bool)
    for x, y, bx, by in sensors:
        manhattan = abs(bx-x) + abs(by-y) - abs(line-y)
        if y == line:
            sensors_on_line.add(x)
        if by == line:
            sensors_on_line.add(bx)
        if manhattan > 0:
            for cant in range(x-manhattan, x+manhattan+1):
                cant_be[cant] = True
    for s in sensors_on_line:
        cant_be[s] = False
    return sum(cant_be.values())

if __name__ == "__main__":
    sensors = open("input.txt").read().strip().split("\n")
    sensors_formatted = []
    for sensor in sensors:
        s, b = sensor.split(":")
        sx, sy = s.split(" at ")[1].split(", ")
        bx, by = b.split(" at ")[1].split(", ")
        sensors_formatted.append((int(sx[2:]), int(sy[2:]), int(bx[2:]), int(by[2:])))
    print(find_covered(sensors_formatted, 2000000))

