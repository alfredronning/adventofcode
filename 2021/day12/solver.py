from collections import defaultdict

def search_caves(current, neighbours, visited):
    visited = visited + [current]
    if current == "end":
        return 1
    res = 0
    for neighbour in neighbours[current]:
        if neighbour in visited and neighbour.islower():
            continue
        res += search_caves(neighbour, neighbours, visited)
    return res

if __name__ == "__main__":
    caves = open("input.txt").read().strip().split("\n")
    neighbours = defaultdict(list)
    for path in caves:
        cave_from, cave_to = path.split("-")
        neighbours[cave_from].append(cave_to)
        neighbours[cave_to].append(cave_from)
    print(search_caves("start", neighbours, []))

