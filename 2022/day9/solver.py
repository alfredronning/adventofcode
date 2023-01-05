def make_step(head, direction):
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    if direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1

if __name__ == "__main__":
    steps = [[step.split()[0], int(step.split()[1])] for step in open("input.txt").read().strip().split("\n")]
    head = [0, 0]
    tail = [0, 0]
    visited = {(0,0)}
    for direction, length in steps:
        for _ in range(length):
            make_step(head, direction)
            xdiff, ydiff = head[0]-tail[0], head[1]-tail[1]
            if abs(xdiff) > 1 or abs(ydiff) > 1:
                tail[0] += 1 if xdiff > 0 else -1 if xdiff < 0 else 0
                tail[1] += 1 if ydiff > 0 else -1 if ydiff < 0 else 0
                visited.add(tuple(tail))
    print(len(visited))

