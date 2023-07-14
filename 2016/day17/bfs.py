from hashlib import md5
POS_MAP = {0: "U", 1: "D", 2: "L", 3: "R"}

def find_shortest(inp, start, vault):
    queue = [(start, "")]
    best = 0
    while len(queue):
        pos, path = queue.pop()
        if pos == vault:
            if len(path) > best:
                best = len(path)
            continue
        doors_open = [c in "bcdef" for c in md5((inp+path).encode()).hexdigest()[:4]]
        valid_neighbours = []
        for d in [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]:
            n = (pos[0]+d[0], pos[1]+d[1], d[2])
            if n[0]>=0 and n[0]<=vault[0] and n[1]>=0 and n[1]<=vault[1] and doors_open[n[2]]:
                valid_neighbours.append(n)
        for neighbour in valid_neighbours:
            queue.append(((neighbour[0], neighbour[1]), path+POS_MAP[neighbour[2]]))
    return best

if __name__ == "__main__":
    inp = "udskfozm"
    initial_pos = (0, 0)
    vault = (3, 3)
    print(find_shortest(inp, initial_pos, vault))

