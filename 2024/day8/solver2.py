from collections import defaultdict

inp = open("input.txt").read().strip().split("\n")

antennas = defaultdict(list)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == ".":
            continue
        antennas[inp[i][j]].append((i, j))

antidotes = set()

for a in antennas:
    locations = antennas[a]
    for i, l1 in enumerate(locations):
        for l2 in locations[i+1:]:
            dx = l2[0]-l1[0]
            dy = l2[1]-l1[1]
            pos = l2
            while pos[0] >= 0 and pos[0] < len(inp) and pos[1] >= 0 and pos[1] < len(inp[0]):
                antidotes.add(pos)
                pos = (pos[0] + dx, pos[1] + dy)
            pos = l2
            while pos[0] >= 0 and pos[0] < len(inp) and pos[1] >= 0 and pos[1] < len(inp[0]):
                antidotes.add(pos)
                pos = (pos[0] - dx, pos[1] - dy)

print(len(antidotes))

