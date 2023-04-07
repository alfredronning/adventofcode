if __name__ == "__main__":
    wires = open("input.txt").read().strip().split("\n")
    min_intersection = float("inf")
    points = set()
    directionmap = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    wire = wires[0]
    current_pos = (0, 0)
    for path in wire.split(","):
        direction, length = directionmap[path[0]], int(path[1:])
        for _ in range(length):
            current_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            points.add(current_pos)

    wire = wires[1]
    current_pos = (0, 0)
    for path in wire.split(","):
        direction, length = directionmap[path[0]], int(path[1:])
        for _ in range(length):
            current_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            if current_pos in points:
                min_intersection = min(min_intersection, abs(current_pos[0])+abs(current_pos[1]))
    print(min_intersection)
    
