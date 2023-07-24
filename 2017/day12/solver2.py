def traverse(connections, current, visited):
    non_visited_neighbours = [n for n in connections[current] if n not in visited]
    visited.add(current)
    for neighbour in non_visited_neighbours:
        traverse(connections, neighbour, visited)


if __name__ == "__main__":
    pipes = open("input.txt").read().strip().split("\n")

    connections = {}
    for pipe in pipes:
        from_program, to_programs = pipe.split(" <-> ")
        if from_program not in connections:
            connections[from_program] = set()
        for to_program in to_programs.split(", "):
            if to_program not in connections:
                connections[to_program] = set()
            connections[from_program].add(to_program)
            connections[to_program].add(from_program)

    visited = set()
    groups = 0
    not_visited = [p for p in connections if p not in visited]
    while len(not_visited):
        groups += 1
        traverse(connections, not_visited[0], visited)
        not_visited = [p for p in connections if p not in visited]
    print(groups)

