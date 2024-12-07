inp = open("input.txt").read().strip().split("\n")

def count_around(grid, i, j):
    res = 0
    for dir in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        x1, x2 = i - dir[0], i + dir[0]
        y1, y2 = j - dir[1], j + dir[1]
        if x1 < 0 or x2 < 0 or x1 >= len(grid) or x2 >= len(grid):
            continue
        if y1 < 0 or y2 < 0 or y1 >= len(grid[0]) or y2 >= len(grid[0]):
            continue
        if grid[x1][y1] == "M" and grid[x2][y2] == "S":
            res += 1
    return res == 2

res = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "A":
            res += count_around(inp, i, j)
print(res)

