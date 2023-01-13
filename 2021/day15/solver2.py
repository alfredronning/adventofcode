from collections import defaultdict

def sorted_insert(open_set, item):
    for i in range(len(open_set)):
        if item[1] <= open_set[i][1]:
            open_set.insert(i, item)
            return
    open_set.insert(len(open_set), item)

def a_star(board, start, end):
    h = lambda x: ((start[0]-end[0])**2 + (start[1]-end[1])**2)**0.5

    visited = set()

    open_set = [(start, h(start))]
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0

    while open_set:
        current, f_score = open_set.pop(0)
        visited.add(current)
        if current == end:
            return g_score[current]
        for direction in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            neighbour = current[0]+direction[0], current[1]+direction[1]
            if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<len(board) and neighbour[1]<len(board[0]):
                tmp_gscore = g_score[current] + board[neighbour[0]][neighbour[1]]
                if tmp_gscore < g_score[neighbour]:
                    g_score[neighbour] = tmp_gscore
                    neighbour_h = tmp_gscore + h(neighbour)
                    if neighbour not in visited:
                        sorted_insert(open_set, (neighbour, neighbour_h))

def upsize_board(board, scale):
    big_board = []
    for i in range(scale):
        for row in board:
            new_row = []
            for j in range(scale):
                new_row += [(n+i+j-1)%9+1 for n in row]
            big_board.append(new_row)
    return big_board
        
if __name__ == "__main__":
    board = [[int(n) for n in row] for row in open("input.txt").read().strip().split("\n")]
    board = upsize_board(board, 5)
    start = (0, 0)
    end = (len(board)-1, len(board[0])-1)
    safest = a_star(board, start, end)
    print(safest)

