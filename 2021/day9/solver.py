def get_point_score(board, point):
    current = board[point[0]][point[1]]
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbour = point[0]+direction[0], point[1]+direction[1]
        if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<len(board) and neighbour[1]<len(board[0]):
            if current >= board[neighbour[0]][neighbour[1]]:
                return 0
    return current + 1

if __name__ == "__main__":
    board = [[int(n) for n in row] for row in open("input.txt").read().strip().split("\n")]
    res = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            res += get_point_score(board, (i, j))
    print(res)

