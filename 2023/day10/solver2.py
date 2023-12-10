def is_connected_pipe(pipetypes, current, neighbour):
    pipe_pair = pipetypes[current]+pipetypes[neighbour]
    if neighbour[0]-current[0] == 1:
        return pipe_pair in ["||", "|J", "|L", "F|", "FJ", "FL", "7|", "7J", "7L", "|S", "FS", "7S", "S|", "SJ", "SL"]
    if neighbour[0]-current[0] == -1:
        return pipe_pair in ["||", "J|", "L|", "|F", "JF", "LF", "|7", "J7", "L7", "S|", "SF", "S7", "|S", "JS", "LS"]
    if neighbour[1]-current[1] == 1:
        return pipe_pair in ["--", "-7", "-J", "F-", "FJ", "F7", "L-", "L7", "LJ", "-S", "LS", "FS", "S-", "S7", "SJ"]
    if neighbour[1]-current[1] == -1:
        return pipe_pair in ["--", "7-", "J-", "-F", "JF", "7F", "-L", "7L", "JL", "S-", "SL", "SF", "-S", "7S", "JS"]

def find_neighbours(pipetypes, current):
    neighbours = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = (current[0]+d[0], current[1]+d[1])
        if neighbour not in pipetypes:
            continue
        if is_connected_pipe(pipetypes, current, neighbour):
            neighbours.append(neighbour)
    return neighbours

def get_loop(inp):
    pipetypes = dict()
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == ".":
                continue
            else:
                pipetypes[(i, j)] = inp[i][j]
    visited = set()
    animal_pos = [pipe for pipe in pipetypes if pipetypes[pipe] == "S"][0]
    queue = [(animal_pos, [])]
    while queue:
        current, current_path = queue.pop()
        visited.add(current)
        neighbours = find_neighbours(pipetypes, current)
        if not neighbours:
            continue
        for neighbour in neighbours:
            if neighbour == animal_pos and len(visited) > 2:
                return current_path
            if neighbour in visited:
                continue
            queue.append((neighbour, current_path + [neighbour]))

def traverse_area(pos, pipes, visited, minx, miny, maxx, maxy):
    queue = [pos]
    count = 0
    while queue:
        current = queue.pop()
        if current in visited:
            continue
        count += 1
        visited.add(current)
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour = (current[0]+d[0], current[1]+d[1])
            if neighbour[0] < minx or neighbour[1] < miny or neighbour[0] >= maxx or neighbour[1] >= maxy:
                return 0
            if neighbour in visited:
                continue
            if neighbour in pipes:
                continue
            queue.append(neighbour)
    return count

def is_left_closed(loop, maxx):
    for i in range(len(loop)-1):
        pipe = loop[i]
        next_pipe = (loop+[loop[0]])[i+1]
        direction_y = next_pipe[1]-pipe[1]
        if pipe[0]+1 > maxx:
            return direction_y == 1

def calculate_enclosed(loop):
    minx = miny = float("inf")
    maxx = maxy = -float("inf")
    for x, y in loop:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    pipes = set(loop)
    left_closed = is_left_closed(loop, maxx)
    enclosed = set()
    for i in range(len(loop)-1):
        pipe = loop[i]
        next_pipe = (loop+[loop[0]])[i+1]
        direction = (next_pipe[0]-pipe[0], next_pipe[1]-pipe[1])
        if direction[0] == -1:
            neighbour = (pipe[0], pipe[1]-(1 if left_closed else -1))
        elif direction[0] == 1:
            neighbour = (pipe[0], pipe[1]+(1 if left_closed else -1))
        elif direction[1] == -1:
            neighbour = (pipe[0]+(1 if left_closed else -1), pipe[1])
        else:
            neighbour = (pipe[0]-(1 if left_closed else -1), pipe[1])
        if neighbour not in pipes:
            enclosed.add(neighbour)
    visited = set()
    res = 0
    for pos in enclosed:
        res += traverse_area(pos, pipes, visited, minx, miny, maxx, maxy)
    return res

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    loop = get_loop(inp)
    print(calculate_enclosed(loop))

