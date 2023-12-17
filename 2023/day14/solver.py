def tilt(rounded, stationary, direction):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)][direction]
    new_rounded = set()

    for round in sorted(list(rounded), key=lambda r: r[0]*-d[0]+r[1]*-d[1]):
        while True:
            new_round = (round[0]+d[0], round[1]+d[1])
            if new_round in stationary or new_round in new_rounded:
                break
            round = new_round
        new_rounded.add(round)
    return new_rounded

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    board = ["#"+r+"#" for r in board]
    board = ["#"*len(board[0])] + board + ["#"*len(board[0])]
    rounded = set()
    stationary = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue
            if board[i][j] == "O":
                rounded.add((i, j))
            else:
                stationary.add((i, j))

    rounded = tilt(rounded, stationary, 0)
    res = 0
    for round in rounded:
        res += (len(board) - round[0])-1
    print(res)

