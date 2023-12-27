from collections import defaultdict

def find_shortest_path(mace, portals, start, end):
    queue = [(start, [], 0)]
    shortest = float("inf")
    while queue:
        current, path, warps = queue.pop()
        if current == end:
            shortest = min(shortest, len(path)+warps)
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n in portals and n not in path:
                n = portals[n]
                warps += 1
            if n in path:
                continue
            if n[0] < 0 or n[1] < 0 or n[0] >= len(mace) or n[1] >= len(mace[0]):
                continue
            if mace[n[0]][n[1]] != ".":
                continue
            queue.append((n, path+[current], warps)) #type: ignore
    return shortest


if __name__ == "__main__":
    mace = open("input.txt").read().split("\n")[:-1]
    portal_spots = defaultdict(list)
    start = (0, 0)
    end = (0, 0)
    for i, row in enumerate(mace[2:-2]):
        for j, tile in enumerate(row[2:-2]):
            if tile != ".":
                continue
            portal_name = None
            i_o, j_o= i+2, j+2
            if mace[i_o-1][j_o].isalpha():
                portal_name = mace[i_o-2][j_o]+mace[i_o-1][j_o]
            if mace[i_o+1][j_o].isalpha():
                portal_name = mace[i_o+1][j_o]+mace[i_o+2][j_o]
            if mace[i_o][j_o-1].isalpha():
                portal_name = mace[i_o][j_o-2]+mace[i_o][j_o-1]
            if mace[i_o][j_o+1].isalpha():
                portal_name = mace[i_o][j_o+1]+mace[i_o][j_o+2]
            if portal_name is None:
                continue
            if portal_name == "AA":
                start = (i, j)
            elif portal_name == "ZZ":
                end = (i, j)
            else:
                portal_spots[portal_name].append((i, j))
    portals = dict()
    for portal in portal_spots.values():
        portals[portal[0]] = portal[1]
        portals[portal[1]] = portal[0]
    print(find_shortest_path([l[2:-2] for l in mace[2:-2]], portals, start, end))



