from collections import deque

inp = open("input.txt").read().strip().split("\n")
dim = 70

felt_at = dict(((int(point.split(",")[0]), int(point.split(",")[1])), i) for i, point in enumerate(inp))

def sorted_add(queue, best, h, point, stop):
    rem = abs(stop[0]-point[0])+abs(stop[1]-point[1])
    current_h = best[point] + rem
    h[point] = current_h
    for i in range(len(queue)):
        if current_h < h[queue[i]]:
            queue.insert(i, point)
            return
    queue.append(point)

def no_path(felt, start, stop, dim, timestep):
    queue = deque([start])
    best = dict()
    h = dict()
    best[start] = 0
    h[start] = abs(stop[0]-start[0])+abs(stop[1]-start[1])

    while queue:
        current = queue.popleft()
        if current == stop:
            return False
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next = (current[0]+d[0], current[1]+d[1])
            if next[0] < 0 or next[1] < 0 or next[0] > dim or next[1] > dim:
                continue
            if next in best and best[next] <= best[current] + 1:
                continue
            if next in felt and felt[next] <= timestep:
                continue
            best[next] = best[current] + 1
            sorted_add(queue, best, h, next, stop)
    return True

lower = 0
upper = float("inf")
time = 1000
while upper-lower > 1:
    blocked = no_path(felt_at, (0, 0), (dim, dim), dim, time)
    if blocked:
        upper = time
        time = (time + lower) // 2
    else:
        lower = time
        if upper == float("inf"):
            time = time*2
        else:
            time = (time + upper) // 2
print(upper)
for point in felt_at:
    if felt_at[point] == upper:
        print(",".join(str(i) for i in point))
