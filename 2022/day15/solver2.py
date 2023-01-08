def find_covered(sensors, sensorpos, size):
    for line in range(size):
        sensors_on_line = set()
        covered_segments = []
        for x, y, d in sensors:
            manhattan = d - abs(line-y)
            if manhattan > 0:
                covered_segments.append((max(0, x-manhattan), min(size, x+manhattan+1)))
        covered_segments.sort()
        checkedx = 0
        for i in range(len(covered_segments)-1):
            if covered_segments[i][0] > checkedx:
                for x in range(checkedx, covered_segments[i][0]):
                    if (x, line) not in sensors_on_line:
                        return 4000000 * x + line
            checkedx = max(checkedx, covered_segments[i][1])

if __name__ == "__main__":
    sensors = open("input.txt").read().strip().split("\n")
    sensors_formatted = []
    sensorpos = set()
    for sensor in sensors:
        s, b = sensor.split(":")
        sx, sy = [int(v[2:]) for v in s.split(" at ")[1].split(", ")]
        bx, by = [int(v[2:]) for v in b.split(" at ")[1].split(", ")]
        d = abs(bx-sx) + abs(by-sy)
        sensors_formatted.append((sx, sy, d))
        sensorpos.add((sx, sy))
        sensorpos.add((bx, by))
    print(find_covered(sensors_formatted, sensorpos, 4000000))
