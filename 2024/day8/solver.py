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
            if dx/3 == dx//3 and dy/3 == dy//3:
                antidotes.add((l1[0] + dx//3, l1[1] + dy//3))
                antidotes.add((l1[0] + 2*dx//3, l1[1] + 2*dy//3))
            antidotes.add((l1[0] + 2*dx, l1[1] + 2*dy))
            antidotes.add((l1[0] - dx, l1[1] - dy))


antidotes_in_bounds = [a for a in antidotes if a[0] >= 0 and a[1] >= 0 and a[0] < len(inp) and a[1] < len(inp[0])]
print(len(antidotes_in_bounds))

