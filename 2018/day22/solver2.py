from collections import defaultdict

def find_region_type(pos, e, regions, depth):
    x, y = pos
    if (x, y) in regions:
        return regions[(x, y)]
    if (x, y) == target:
        g = 0
    elif x == 0:
        g = y*48271
    elif y == 0:
        g = x*16807
    else:
        if (x-1, y) not in e:
            find_region_type((x-1, y), e, regions, depth)
        if (x, y-1) not in e:
            find_region_type((x, y-1), e, regions, depth)
        g = e[(x-1,y)]*e[(x,y-1)]
    new_e = (g+depth)%20183
    e[(x,y)] = new_e
    regions[(x,y)] = new_e%3
    return regions[(x, y)]

def sorted_add(open_set, scores, time, came_from, current, new_region, step, h):
    if time[current]+step < time[new_region]:
        time[new_region] = time[current]+step
        scores[new_region] = time[current]+step+h(new_region[0])
        came_from[new_region] = current
        if new_region not in open_set:
            for i, cmp_item in enumerate(open_set):
                if scores[new_region] < scores[cmp_item]:
                    open_set.insert(i, new_region)
                    return
            open_set.append(new_region)

def print_board(size, e, regions, end, depth, came_from):
    path = []
    current = (end, 0)
    while came_from[current]:
        path.append(current)
        current = came_from[current]
    m = 20183
    for y in range(size[0]+1):
        row = ""
        for x in range(size[1]+1):
            if (x, y) == (0, 0):
                row += "M"
            elif (x, y) == end:
                row += "T"
            elif (x, y) in [p[0] for p in path]:
                row += str([p[1] for p in path if p[0] == (x, y)][0])
            else:
                r = find_region_type((x, y), e, regions, depth, m)
                row += ".=|"[r]
        print(row)
    print(path[::-1])

def a_star(start, end, depth):
    h = lambda pos: 1*abs(end[0]-pos[0])+abs(end[1]-pos[1])
    regions = dict()
    erosion_level = dict()
    came_from = {(start, 0):None}

    open_set = [(start, 0)]

    time = defaultdict(lambda: float("inf"))
    scores = defaultdict(lambda: float("inf"))
    time[(start, 0)] = 0
    time[(start, 1)] = 0
    time[(start, 2)] = 0
    scores[(start, 0)] = h(start)

    while open_set:
        current = open_set.pop(0)
        current_pos, current_tool = current
        if current_pos == end:
            if current_tool == 0:
                #print_board((end[1]+20, end[0]+20), erosion_level, regions, end, depth, came_from)
                return time[(end, current_tool)]
            else:
                new_region = (current_pos, 0)
                sorted_add(open_set, scores, time, came_from, current, new_region, 7, h)
                continue
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbour = (current_pos[0]+d[0], current_pos[1]+d[1])
            if neighbour[0] < 0 or neighbour[1] < 0:
                continue
            neighbour_type = find_region_type(neighbour, erosion_level, regions, depth)
            if (current_tool+1)%3 == neighbour_type:
                current_type = find_region_type(current_pos, erosion_level, regions, depth)
                types = (neighbour_type, current_type)
                new_tool = 0 if 1 not in types else 1 if 2 not in types else 2
                new_region = (neighbour, new_tool)
                sorted_add(open_set, scores, time, came_from, current, new_region, 8, h)
            else:
                new_region = (neighbour, current_tool)
                sorted_add(open_set, scores, time, came_from, current, new_region, 1, h)
    raise Exception("Goal not reachable")

if __name__ == "__main__":
    start = (0, 0)
    target = (15,740)
    depth = 3558

    #target = (10, 10)
    #depth = 510

    print(a_star(start, target, depth))
