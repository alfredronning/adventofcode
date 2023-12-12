def parse_board(board):
    walls = set()
    lower_keys = {}
    upper_keys = {}
    start = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            tile = board[i][j]
            if tile == "#":
                walls.add((i, j))
            elif tile == "@":
                start = (i, j)
            elif tile.islower():
                lower_keys[(i, j)] = tile
            elif tile.isupper():
                upper_keys[(i, j)] = tile.lower()
    return start, walls, lower_keys, upper_keys

def find_distances(start, walls, lower_keys, upper_keys, keys_gathered):
    reachable = []
    visited = set()
    queue = [start]
    dists = {}
    dists[start] = 0
    while queue:
        queue.sort(key=lambda x: -dists[x])
        current = queue.pop()
        visited.add(current)
        for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n in walls:
                continue
            if n in upper_keys and upper_keys[n] not in keys_gathered:
                continue
            if n in visited:
                continue
            if n in lower_keys and lower_keys[n] not in keys_gathered:
                reachable.append(n)
            if n not in dists or dists[current]+1 < dists[n]:
                dists[n] = dists[current]+1
                if n not in queue:
                    queue.append(n)
    return reachable, dists


def find_shortest_path(start, walls, lower_keys, upper_keys, keys_gathered, dist, cache):
    if dist >= cache["best"]:
        return float("inf")
    cache_key = "".join(sorted(keys_gathered))+str(start[0])+str(start[1])
    if cache_key in cache and dist >= cache[cache_key]:
        return float("inf")
    cache[cache_key] = dist
    if len(keys_gathered) == len(lower_keys):
        cache["best"] = min(cache["best"], dist)
        return dist
    reachable, dists = find_distances(start, walls, lower_keys, upper_keys, keys_gathered)
    min_d = float("inf")
    for r in reachable:
        d = find_shortest_path(r, walls, lower_keys, upper_keys, keys_gathered+[lower_keys[r]], dist+dists[r], cache)
        min_d = min(min_d, d)
    return min_d


if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    start, walls, lower_keys, upper_keys = parse_board(board)

    cache = {}
    cache["best"] = 3300
    print(find_shortest_path(start, walls, lower_keys, upper_keys, [], 0, cache))

