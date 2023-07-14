from hashlib import md5
POS_MAP = {0: "U", 1: "D", 2: "L", 3: "R"}

def find_shortest(inp, pos, vault, path, cache):
    if len(path) >= cache["best"]:
        return
    if pos == vault:
        cache["best"] = len(path)
        cache["path"] = path
        return
    doors_open = [c in "bcdef" for c in md5((inp+path).encode()).hexdigest()[:4]]
    valid_neighbours = []
    for d in [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]:
        n = (pos[0]+d[0], pos[1]+d[1], d[2])
        if n[0]>=0 and n[0]<=vault[0] and n[1]>=0 and n[1]<=vault[1] and doors_open[n[2]]:
            valid_neighbours.append(n)
    valid_neighbours.sort(key=lambda n: (n[0]-vault[0])**2+(n[1]-vault[1])**2)
    for neighbour in valid_neighbours:
        find_shortest(inp, (neighbour[0], neighbour[1]), vault, path+POS_MAP[neighbour[2]], cache)

if __name__ == "__main__":
    inp = "udskfozm"
    initial_pos = (0, 0)
    vault = (3, 3)

    cache = {"best": float("inf")}
    find_shortest(inp, initial_pos, vault, "", cache)
    if "path" not in cache:
        raise Exception("Not possible with that passcode")
    print(cache["path"])

