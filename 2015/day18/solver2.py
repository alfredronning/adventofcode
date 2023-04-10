def simulate_lights(lights, size):
    off_neighbour_on_counts = dict()
    next_lights = cornerset(size)
    for light in on_lights:
        neightbour_on_count = 0
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            neightbour = (light[0]+d[0], light[1]+d[1])
            if 0 <= neightbour[0] < size and 0 <= neightbour[1] < size:
                if neightbour in lights:
                    neightbour_on_count += 1
                else:
                    if neightbour in off_neighbour_on_counts:
                        off_neighbour_on_counts[neightbour] += 1
                    else:
                        off_neighbour_on_counts[neightbour] = 1
        if neightbour_on_count in [2, 3]:
            next_lights.add(light)
    for light in off_neighbour_on_counts:
        if off_neighbour_on_counts[light] == 3:
            next_lights.add(light)
    return next_lights

def cornerset(size):
    s = set()
    s.add((0, 0))
    s.add((0, size-1))
    s.add((size-1, 0))
    s.add((size-1, size-1))
    return s

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    size = len(inp)
    on_lights = cornerset(size)
    for i, row in enumerate(inp):
        for j, light in enumerate(row):
            if light == "#":
                on_lights.add((i, j))
    for _ in range(100):
        on_lights = simulate_lights(on_lights, size)
    print(len(on_lights))
    
