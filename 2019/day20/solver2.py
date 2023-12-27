from collections import defaultdict
import heapq

def find_shortest_path(portals, is_outer_portal, start, end):
    queue = []
    heapq.heappush(queue, (0, 0, start, []))
    while queue:
        l, level, current, path = heapq.heappop(queue)
        if current == end and level == 0:
            return l
        for n, dist in portals[current]:
            if n == end:
                n_level = level
            else:
                n_level = level + (-1 if is_outer_portal[n] else 1)
            if n_level < 0:
                continue
            if (n, n_level) not in path:
                heapq.heappush(queue, (l+dist, n_level, n, path+[(current, level)]))


def calc_dists(mace, portals, start, end):
    neighbour_portal_dists = defaultdict(list)
    for point in list(portals.keys())+[start]:
        visited = set()
        queue = [(0, point)]
        while queue:
            dist, current = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            if current == end:
                neighbour_portal_dists[point].append((current, dist))
                continue
            if current in portals and current != point:
                neighbour_portal_dists[point].append((portals[current], dist+1))
                continue
            for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                n = (current[0]+d[0], current[1]+d[1])
                if n[0] < 0 or n[1] < 0 or n[0] >= len(mace) or n[1] >= len(mace[0]):
                    continue
                if mace[n[0]][n[1]] != ".":
                    continue
                heapq.heappush(queue, (dist+1, n)) # type: ignore
    return neighbour_portal_dists


if __name__ == "__main__":
    mace = open("input.txt").read().split("\n")[:-1]
    portal_spots = defaultdict(list)
    start = (0, 0)
    end = (0, 0)
    is_outer_portal = dict()
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
                if i==0 or j==0 or i+5==len(mace) or j+5==len(mace[0]):
                    is_outer_portal[(i, j)] = False
                else:
                    is_outer_portal[(i, j)] = True
                portal_spots[portal_name].append((i, j))
    mace = [l[2:-2] for l in mace[2:-2]]
    portals = dict()
    for portal in portal_spots.values():
        portals[portal[0]] = portal[1]
        portals[portal[1]] = portal[0]
    neighbour_portal_dists = calc_dists(mace, portals, start, end)
    print(find_shortest_path(neighbour_portal_dists, is_outer_portal, start, end))

