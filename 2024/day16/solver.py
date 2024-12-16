from collections import defaultdict, deque

maze = open("input.txt").read().strip().split("\n")
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start = (0, 0)
end = (0, 0)
walls = set()
for i, row in enumerate(maze):
    for j, tile in enumerate(row):
        if tile == "S":
            start = (i, j)
        elif tile == "E":
            end = (i, j)
        elif tile == "#":
            walls.add((i, j))

def best_path(walls, start, end):
    open_set = deque([(start, int(1))])

    scores = defaultdict(lambda: float("inf"))
    scores[(start, 1)] = 0

    while open_set:
        pos, dir = open_set.popleft()
        for d in [1, -1]:
            turn = (pos, (dir+d)%4)
            if turn not in scores or scores[turn] > scores[(pos, dir)] + 1000:
                scores[turn] = scores[(pos, dir)] + 1000
                open_set.append(turn)
        forward = ((pos[0] + D[dir][0], pos[1] + D[dir][1]), dir)
        if forward[0] not in walls:
            if forward not in scores or scores[forward] > scores[(pos, dir)] + 1:
                scores[forward] = scores[(pos, dir)] + 1
                open_set.append(forward)
    end_dims = [(end, i) for i in range(4)]
    best = min(end_dims, key=lambda x: scores[x])
    return scores[best]

print(best_path(walls, start, end))
