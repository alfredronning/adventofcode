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

def get_loop_size(inp):
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
                return len(current_path) + 1
            if neighbour in visited:
                continue
            queue.append((neighbour, current_path + [current]))
    raise Exception("no loop from S")

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    loop_size = get_loop_size(inp)
    print(-(-loop_size-1)//2)
    
