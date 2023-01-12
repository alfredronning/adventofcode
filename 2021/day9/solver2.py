def is_lowpoint(board, point):
    current = board[point[0]][point[1]]
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbour = point[0]+direction[0], point[1]+direction[1]
        if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<len(board) and neighbour[1]<len(board[0]):
            if current >= board[neighbour[0]][neighbour[1]]:
                return 0
    return current + 1

def find_basin_size(board, point, visited):
    visited.add(point)
    current = board[point[0]][point[1]]
    if current == 9:
        return 0
    res = 1
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbour = point[0]+direction[0], point[1]+direction[1]
        if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<len(board) and neighbour[1]<len(board[0]):
            if neighbour not in visited:
                res += find_basin_size(board, neighbour, visited)
    return res

if __name__ == "__main__":
    board = [[int(n) for n in row] for row in open("input.txt").read().strip().split("\n")]
    lowpoints = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_lowpoint(board, (i, j)):
                lowpoints.append((i, j))
    basins = []
    for lowpoint in lowpoints:
        basins.append(find_basin_size(board, lowpoint, set()))
    res = 1
    basins.sort()
    for i in range(1, 4):
        res *= basins[-i]
    print(res)

