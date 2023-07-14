from collections import defaultdict
import time

def valid_neighbour(board, n):
    if n[0] < 1 or n[0] >= len(board)-1 or n[1] < 1 or n[1] >= len(board[0])-1:
        return False
    return board[n[0]][n[1]] != "#"

def sorted_add(open_set, scores, item):
    for i, cmp_item in enumerate(open_set):
        if scores[item] < scores[cmp_item]:
            open_set.insert(i, item)
            return
    open_set.append(item)

def a_star(board, start, end, h):
    open_set = [start]
    came_from = {start: None}

    length = defaultdict(lambda: float("inf"))
    length[start] = 0

    scores = defaultdict(lambda: float("inf"))
    scores[start] = h(start, end)

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
            if valid_neighbour(board, neighbour):
                if length[current]+1 < length[neighbour]:
                    came_from[neighbour] = current
                    length[neighbour] = length[current]+1
                    scores[neighbour] = length[current]+1+h(neighbour, end)
                    if neighbour not in open_set:
                        sorted_add(open_set, scores, neighbour)
    raise Exception("Goal not reachable")

def find_shortest_path(distances, current, path, visited, locations):
    if len(visited) == len(locations):
        return path + distances[(0, current)]
    next_locations = [l for l in locations if l not in visited]
    best = float("inf")
    for location in next_locations:
        dist = distances[tuple(sorted([current, location]))]
        path_total = find_shortest_path(distances, location, path+dist, visited+[location], locations)
        best = min(best, path_total)
    return best

if __name__ == "__main__":
    t0 = time.time()
    board = open("input.txt").read().strip().split("\n")
    locations = "01234567"
    positions = dict()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in locations:
                positions[int(board[row][col])] = (row, col)

    h = lambda pos, end: ((end[0]-pos[0])**2+(end[1]-pos[1])**2)**0.5
    t1 = time.time()
    distances = dict()
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            distances[(i, j)] = a_star(board, positions[i], positions[j], h)
    t2 = time.time()
    shortest_path = find_shortest_path(distances, 0, 0, [0], [int(l) for l in locations])
    print(shortest_path)
    t3 = time.time()
    print("init time", t1-t0)
    print("astar time", t2-t1)
    print("dfs time", t3-t2)

