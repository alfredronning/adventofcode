inp = open("input.txt").read().strip().split("\n")

def count_around(grid, i, j):
    res = 0
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        x0, x1, x2 = i - 2*dir[0], i - dir[0], i + dir[0]
        y0, y1, y2 = j - 2*dir[1], j - dir[1], j + dir[1]
        if x0 < 0 or x1 < 0 or x2 < 0 or x0 >= len(grid) or x1 >= len(grid) or x2 >= len(grid):
            continue
        if y0 < 0 or y1 < 0 or y2 < 0 or y0 >= len(grid[0]) or y1 >= len(grid[0]) or y2 >= len(grid[0]):
            continue
        if grid[x0][y0] == "X" and grid[x1][y1] == "M" and grid[x2][y2] == "S":
            res += 1
    return res

res = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "A":
            res += count_around(inp, i, j)
print(res)

