if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    visited = set()
    pos = [0, 0]
    for direction in inp:
        if direction == "^":
            pos[0] += 1
        elif direction == "v":
            pos[0] -= 1
        elif direction == ">":
            pos[1] += 1
        elif direction == "<":
            pos[1] -= 1
        visited.add((pos[0], pos[1]))
    print(len(visited))

