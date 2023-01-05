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
    knots = [[0, 0] for _ in range(10)]
    visited = {(0, 0)}
    for d, l in steps:
        for _ in range(int(l)):
            make_step(knots[0], d)
            for i in range(9):
                head, tail = knots[i], knots[i+1]
                xdiff, ydiff = head[0]-tail[0], head[1]-tail[1]
                if abs(xdiff) > 1 or abs(ydiff) > 1:
                    tail[0] += 1 if xdiff > 0 else -1 if xdiff < 0 else 0
                    tail[1] += 1 if ydiff > 0 else -1 if ydiff < 0 else 0
            visited.add(tuple(knots[-1]))
    print(len(visited))

