if __name__ == "__main__":
    wires = open("input.txt").read().strip().split("\n")
    min_intersection = float("inf")
    points = dict()
    directionmap = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    wire = wires[0]
    current_pos = (0, 0)
    time = 0
    for path in wire.split(","):
        direction, length = directionmap[path[0]], int(path[1:])
        for _ in range(length):
            time += 1
            current_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            if current_pos not in points:
                points[current_pos] = time

    wire = wires[1]
    current_pos = (0, 0)
    time = 0
    for path in wire.split(","):
        direction, length = directionmap[path[0]], int(path[1:])
        for _ in range(length):
            time += 1
            current_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            if current_pos in points:
                min_intersection = min(min_intersection, time+points[current_pos])
    print(min_intersection)
    

