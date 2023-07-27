from collections import defaultdict

def split_ors(regex):
    splits = []
    depth = 1
    previous_end = 1
    for i in range(1, len(regex)):
        current = regex[i]
        if current == "(":
            depth += 1
        elif current == ")":
            depth -= 1
            if depth == 0:
                splits.append(regex[previous_end: i])
                previous_end = i+1
                break
        elif current == "|" and depth == 1:
            splits.append(regex[previous_end: i])
            previous_end = i+1
    return [split+regex[previous_end:] for split in splits]


def do_moves(regex, pos, doors):
    for move in regex:
        if move == "W":
            next_pos = (pos[0], pos[1]-1)
        elif move == "E":
            next_pos = (pos[0], pos[1]+1)
        elif move == "N":
            next_pos = (pos[0]-1, pos[1])
        else:
            next_pos = (pos[0]+1, pos[1])
        doors[pos].add(next_pos)
        doors[next_pos].add(pos)
        pos = next_pos
    return pos
    

def find_doors(regex, doors):
    startpos = (0, 0)
    queue = [(regex, startpos)]
    pointer = 0

    while pointer < len(queue):
        current, pos = queue[pointer]
        pointer += 1
        if current == "":
            continue
        if current[0] == "(":#)
            ors = split_ors(current)
            for o in ors:
                if (o, pos) not in queue:
                    queue.append((o, pos))
        else:
            if "(" not in current:#)
                do_moves(current, pos, doors)
            else:
                split = current.index("(")#)
                moves, rest = current[:split], current[split:]
                next_pos = do_moves(moves, pos, doors)
                if (rest, next_pos) not in queue:
                    queue.append((rest, next_pos)) # type: ignore


def dijkstas(doors, startpos = (0, 0)):
    nodes = [node for node in doors]
    dists = {node: float("inf") for node in nodes}
    visited = {}

    current = startpos
    current_distance = 0
    dists[current] = current_distance
    while True:
        for neighbour in doors[current]:
            if neighbour not in nodes:
                continue
            if current_distance+1 < dists[neighbour]:
                dists[neighbour] = current_distance+1
        dists[current] = current_distance
        visited[current] = current_distance
        nodes.remove(current)
        if not nodes:
            break
        current = sorted(nodes, key=lambda n: dists[n])[0]
        current_distance = dists[current]
    return visited


def print_board(doors, startpos=(0, 0)):
    minx = miny = 100000000
    maxx = maxy = 0
    for x, y in doors:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    board = []
    board.append(["#"]*((maxx-minx+1)*2+1))
    for _ in range(maxy-miny+1):
        board.append(["#"]+[".", "#"]*(maxx-minx+1))
        board.append(["#"]*((maxx-minx+1)*2+1))
    board[(startpos[0]-minx)*2+1][(startpos[1]-miny)*2+1] = "X"
    for f in doors:
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour = (f[0]+d[0], f[1]+d[1])
            if neighbour in doors[f]:
                board[(f[0]-minx)*2+1+d[0]][(f[1]-miny)*2+1+d[1]] = "-" if d[0] != 0 else "|"
    for row in board:
        print("".join(row))


if __name__ == "__main__":
    regex = open("input.txt").read().strip()[1:-1]
    doors = defaultdict(set)
    find_doors(regex, doors)
    distances = dijkstas(doors)
    #print_board(doors)
    print(max(distances.values()))
    print(len([c for c in distances.values() if c >= 1000]))

