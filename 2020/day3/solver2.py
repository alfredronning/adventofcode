if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    trees = set()
    endx = len(board)-1
    boardlen = len(board[0])
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == "#":
                trees.add((i, j))

    total_encountered = []
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        pos = [0, 0]
        encountered_trees = 0
        while pos[0] < endx:
            pos[0] += slope[0]
            pos[1] = (pos[1] + slope[1]) % boardlen
            if (pos[0], pos[1]) in trees:
                encountered_trees += 1
        total_encountered.append(encountered_trees)
    res = 1
    for trees in total_encountered:
        res *= trees
    print(res)

