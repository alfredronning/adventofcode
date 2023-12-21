from collections import deque

def print_board(res, garden):
    for i in range(len(garden)):
        row = ""
        for j in range(len(garden[0])):
            if garden[i][j] == "#":
                row += "#"
            elif (i, j) in res:
                row += "O"
            else:
                row += "."
        print(row)
    print()

if __name__ == "__main__":
    garden = open("input.txt").read().strip().split("\n")
    start = (0, 0)
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j] == "S":
                start = (i, j)

    visited = set()
    steps = 64
    res = set()
    queue = deque()
    queue.append((start, 0))
    while queue:
        current, current_steps = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        if current_steps > steps:
            continue
        if (steps-current_steps)%2 == 0:
            res.add(current)
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n[0] < 0 or n[1] < 0 or n[0] >= len(garden) or n[1] >= len(garden[0]):
                continue
            if garden[n[0]][n[1]] == "#":
                continue
            queue.append((n, current_steps+1))
    print(len(res))
