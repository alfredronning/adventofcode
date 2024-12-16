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

    points = defaultdict(lambda: float("inf"))
    came_from = defaultdict(list)
    points[(start, 1)] = 0

    while open_set:
        pos, dir = open_set.popleft()
        for d in [1, -1]:
            turn = (pos, (dir+d)%4)
            turn_points = points[(pos, dir)] + 1000
            if turn not in points or points[turn] >= turn_points:
                if turn_points < points[turn]:
                    came_from[turn] = [(pos, dir)]
                else:
                    came_from[turn].append((pos, dir))
                points[turn] = turn_points
                open_set.append(turn)
        forward = ((pos[0] + D[dir][0], pos[1] + D[dir][1]), dir)
        forward_points = points[(pos, dir)] + 1
        if forward[0] not in walls:
            if forward not in points or points[forward] >= forward_points:
                if forward_points < points[forward]:
                    came_from[forward] = [(pos, dir)]
                else:
                    came_from[forward].append((pos, dir))
                points[forward] = forward_points
                open_set.append(forward)

    end_dims = [(end, i) for i in range(4)]
    best = min(points[e] for e in end_dims)
    queue = [e for e in end_dims if points[e] == best]
    visited = set()
    while queue:
        current = queue.pop()
        if current is None or current in visited:
            continue
        visited.add(current)
        queue += came_from[current]
    on_path = set(p[0] for p in visited)
    return len(on_path)

print(best_path(walls, start, end))
