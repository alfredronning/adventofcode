from collections import defaultdict

def valid_neighbour(hills, n_from, n_to):
    if n_to[0] < 0 or n_to[0] >= len(hills) or n_to[1] < 0 or n_to[1] >= len(hills[0]):
        return False
    from_char = hills[n_from[0]][n_from[1]]
    to_char = hills[n_to[0]][n_to[1]]
    from_height = ord("a") if from_char == "S" else ord("z") if from_char == "E" else ord(from_char)
    to_height = ord("a") if to_char == "S" else ord("z") if to_char == "E" else ord(to_char)
    return to_height-from_height <= 1

def sorted_add(open_set, scores, item, h):
    for i, cmp_item in enumerate(open_set):
        if scores[item] < scores[cmp_item]:
            open_set.insert(i, item)
            return
    open_set.append(item)

def print_path(hills, came_from, current):
    hills_cp = [[h for h in row] for row in hills]
    hills_cp[current[0]][current[1]] = "*"
    current = came_from[current]
    while current is not None:
        hills_cp[current[0]][current[1]] = "."
        current = came_from[current]
    for row in hills_cp:
        print("".join(row))
    print()

def a_star(hills, start, end, h):
    open_set = [start]
    came_from = {start: None}

    length = defaultdict(lambda: float("inf"))
    length[start] = 0

    scores = defaultdict(lambda: float("inf"))
    scores[start] = h(start)

    while open_set:
        current = open_set[0]
        if current == end:
            i = 0
            while came_from[current] is not None:
                i += 1
                current = came_from[current]
            return i
        open_set = open_set[1:]
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbour = (current[0]+d[0], current[1]+d[1])
            if valid_neighbour(hills, current, neighbour):
                if length[current]+1 < length[neighbour]:
                    came_from[neighbour] = current
                    length[neighbour] = length[current]+1
                    scores[neighbour] = length[current]+1+h(neighbour)
                    if neighbour not in open_set:
                        sorted_add(open_set, scores, neighbour, h)
    raise Exception("Goal not reachable")

if __name__ == "__main__":
    hills = [[c for c in row] for row in open("input.txt").read().strip().split("\n")]
    start = (0, 0)
    end = (0, 0)
    for i, row in enumerate(hills):
        for j, height in enumerate(row):
            if height == "E":
                end = (i, j)
            if height == "S":
                start = (i, j)
    h = lambda pos: (end[0]-pos[0])**2+(end[1]-pos[1])**2
    print(a_star(hills, start, end, h))

