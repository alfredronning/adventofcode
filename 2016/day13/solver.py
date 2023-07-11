def is_wall(pos, inp):
    x, y = pos
    return "{:b}".format(x*x+3*x+2*x*y+y+y*y+inp).count("1")%2 == 1

def hueristic(pos, goal):
    x0, y0 = pos
    x1, y1 = goal
    return ((x1-x0)**2+(y1-y0)**2)**0.5

def sorted_insert(open_set, node):
    for i in range(len(open_set)):
        if node[1] < open_set[i][1]:
            open_set.insert(i, node)
            return
    open_set.append(node)

def find_shortest(start, goal, inp):
    g_score = dict()
    f_score = dict()
    walls = set()

    g_score[start] = 0
    f_score[start] = hueristic(start, goal)

    open_set = [(start, f_score[start])]
    
    while len(open_set):
        current, _ = open_set.pop(0)
        if current == goal:
            return g_score[current]
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = (current[0]+d[0], current[1]+d[1])
            if neighbour[0] < 0 or neighbour[1] < 0 or neighbour in walls:
                continue
            if is_wall(neighbour, inp):
                walls.add(neighbour)
                continue
            if neighbour not in g_score or g_score[current] + 1 < g_score[neighbour]:
                g_score[neighbour] = g_score[current] + 1
                f_score[neighbour] = g_score[neighbour] + hueristic(neighbour, goal)

                if neighbour not in open_set:
                    sorted_insert(open_set, (neighbour, f_score[neighbour]))
    raise Exception("No path from start to goal")


if __name__ == "__main__":
    inp = 1352
    goal = (31, 39)
    start = (1, 1)
    shortest_path = find_shortest(start, goal, inp)
    print(shortest_path)

