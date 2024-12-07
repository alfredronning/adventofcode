map = open("input.txt").read().strip().split("\n")

obstacles = set()
guard_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard = (0, 0)

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "#":
            obstacles.add((i, j))
        elif map[i][j] == "^":
            guard = (i, j)

guard_path = set()
guard_dir = 0
guard2 = guard
while guard2[0] > 0 and guard2[1] > 0 and guard2[0] < len(map) and guard2[1] < len(map[0]):
    guard_path.add(guard2)
    next = (guard2[0] + guard_dirs[guard_dir][0], guard2[1] + guard_dirs[guard_dir][1])
    if next in obstacles:
        guard_dir = (guard_dir + 1) % 4
    else:
        guard2 = next

print(len(guard_path))

def is_loop(obst, guard):
    visited = set()
    guard_dir = 0

    while guard[0] > 0 and guard[1] > 0 and guard[0] < len(map) and guard[1] < len(map[0]):
        h = (guard[0], guard[1], guard_dir)
        if h in visited:
            return True
        visited.add(h)
        next = (guard[0] + guard_dirs[guard_dir][0], guard[1] + guard_dirs[guard_dir][1])
        if next in obst:
            guard_dir = (guard_dir + 1) % 4
        else:
            guard = next
    return False

res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if (i, j) in obstacles:
            continue
        if (i, j) not in guard_path:
            continue
        obst = obstacles.copy()
        obst.add((i, j))
        res += is_loop(obst, guard)

print(res)
