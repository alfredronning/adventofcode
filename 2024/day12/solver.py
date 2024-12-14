guarden = open("input.txt").read().strip().split("\n")

visited = set()
res = 0

def traverse_from_point(i, j, visited):
    letter = guarden[i][j]
    visited.add((i, j))
    queue = [(i, j)]
    area = 0
    perimiter = 0
    while queue:
        current = queue.pop()
        area += 1
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next = (current[0]+d[0], current[1]+d[1])
            if next[0] < 0 or next[1] < 0 or next[0] >= len(guarden) or next[1] >= len(guarden[0]):
                perimiter += 1
            elif guarden[next[0]][next[1]] != letter:
                perimiter += 1
            else:
                if next in visited:
                    continue
                visited.add(next)
                queue.append(next)
    return area*perimiter

for i in range(len(guarden)):
    for j in range(len(guarden[0])):
        if (i, j) in visited:
            continue
        res += traverse_from_point(i, j, visited)
print(res)
