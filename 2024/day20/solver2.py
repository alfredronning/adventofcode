from collections import deque, defaultdict

board = open("input.txt").read().strip().split("\n")
#board = open("testinput.txt").read().strip().split("\n")
maxx, maxy = 0, 0
start = (0, 0)
end = (0, 0)
path = set()
for i, row in enumerate(board):
    for j, cell in enumerate(row):
        maxx = max(maxx, i)
        maxy = max(maxy, i)
        if cell == ".":
            path.add((i, j))
        elif cell == "S":
            path.add((i, j))
            start = (i, j)
        elif cell == "E":
            path.add((i, j))
            end = (i, j)

def find_shortest(path, start, end):
    queue = deque([end])
    best = defaultdict(lambda:float("inf"))
    best[end] = 0

    while queue:
        current = queue.popleft()
        if current == start:
            continue
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next = (current[0]+d[0], current[1]+d[1])
            if next not in path:
                continue
            if best[next] <= best[current] + 1:
                continue
            best[next] = best[current] + 1
            queue.append(next)
    return best


dists = find_shortest(path, start, end)
res = 0
for current in path:
    for other in path:
        diff = abs(other[0]-current[0])+abs(other[1]-current[1])
        if diff > 20:
            continue
        diff = dists[current]-dists[other]+diff
        if diff <= -100:
            res += 1
print(res)

