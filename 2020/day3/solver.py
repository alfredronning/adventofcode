if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    trees = set()
    endx = len(board)-1
    boardlen = len(board[0])
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == "#":
                trees.add((i, j))

    pos = [0, 0]
    encountered_trees = 0
    while pos[0] < endx:
        pos[0] += 1
        pos[1] = (pos[1] + 3) % boardlen
        if (pos[0], pos[1]) in trees:
            encountered_trees += 1
    print(encountered_trees)

