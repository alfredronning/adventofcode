guarden = open("input.txt").read().strip().split("\n")

visited = set()
res = 0
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def traverse_from_point(i, j, visited):
    letter = guarden[i][j]
    visited.add((i, j))
    queue = [(i, j)]
    area = 0
    sides = 0
    sidesets = [set(), set(), set(), set()]
    while queue:
        current = queue.pop(0)
        area += 1
        for i in range(4):
            d = DIRECTIONS[i]
            next = (current[0]+d[0], current[1]+d[1])
            if next[0] < 0 or next[1] < 0 or next[0] >= len(guarden) or next[1] >= len(guarden[0]) or guarden[next[0]][next[1]] != letter:
                sidesets[i].add(current)
                if i < 2 and (current[0], current[1]-1) not in sidesets[i] and (current[0], current[1]+1) not in sidesets[i]:
                    sides += 1
                elif i >= 2 and (current[0]-1, current[1]) not in sidesets[i] and (current[0]+1, current[1]) not in sidesets[i]:
                    sides += 1
            else:
                if next in visited:
                    continue
                visited.add(next)
                queue.append(next)
    return area*sides

for i in range(len(guarden)):
    for j in range(len(guarden[0])):
        if (i, j) in visited:
            continue
        res += traverse_from_point(i, j, visited)
print(res)

