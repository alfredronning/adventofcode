import re

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    steps = []
    on_set = set()
    for step in inp:
        match = re.findall(r"^(.*)\sx=(.*),y=(.*),z=(.*)", step)[0]
        on = True if match[0] == "on" else False
        coords = [[int(c) for c in point.split("..")] for point in match[1:]]
        steps.append((on, coords))

    for on, coords in steps:
        xr, yr, zr = coords
        xr = (max(-50, xr[0]), min(50, xr[1]))
        yr = (max(-50, yr[0]), min(50, yr[1]))
        zr = (max(-50, zr[0]), min(50, zr[1]))
        if on:
            for x in range(xr[0], xr[1]+1):
                for y in range(yr[0], yr[1]+1):
                    for z in range(zr[0], zr[1]+1):
                        on_set.add((x, y, z))
        else:
            for x in range(xr[0], xr[1]+1):
                for y in range(yr[0], yr[1]+1):
                    for z in range(zr[0], zr[1]+1):
                        if (x, y, z) in on_set:
                            on_set.remove((x, y, z))
    print(len(on_set))



