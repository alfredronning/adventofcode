if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    visited = set()
    pos = [0, 0]
    robot = [0, 0]
    for i, direction in enumerate(inp):
        current = pos if i%2 else robot
        if direction == "^":
            current[0] += 1
        elif direction == "v":
            current[0] -= 1
        elif direction == ">":
            current[1] += 1
        elif direction == "<":
            current[1] -= 1
        visited.add((current[0], current[1]))
    print(len(visited))

