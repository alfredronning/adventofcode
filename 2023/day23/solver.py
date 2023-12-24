def find_longest(board, start, end):
    queue = [(start, [])]
    best = 0
    while queue:
        current, path = queue.pop()
        if current == end:
            best = max(best, len(path))
            continue
        for i in range(4):
            dx, dy = [(1, 0), (-1, 0), (0, 1), (0, -1)][i]
            nx, ny = current[0] + dx, current[1] + dy
            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                continue
            if board[nx][ny] == "#":
                continue
            if board[nx][ny] in ["v", "^", ">", "<"] and board[nx][ny] != ["v", "^", ">", "<"][i]:
                continue
            if (nx, ny) in path:
                continue
            queue.append(((nx, ny), path + [current]))
    return best


if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    start = (0, 1)
    end = (len(board)-1, len(board[0]) - 2)
    print(find_longest(board, start, end))
