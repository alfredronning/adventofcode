def move_cucumbers(cucumbers_right, cucumbers_down, h, w):
    changed = False
    new_cucumbers_right = set()
    not_moved = set()
    for oldpos in cucumbers_right:
        row, col = oldpos
        nextpos = (row, (col+1)%w)
        if not nextpos in cucumbers_down and not nextpos in cucumbers_right:
            new_cucumbers_right.add(nextpos)
            changed = True
        else:
            not_moved.add(oldpos)
    for oldpos in not_moved:
        new_cucumbers_right.add(oldpos)
    new_cucumbers_down= set()
    not_moved = set()
    for oldpos in cucumbers_down:
        row, col = oldpos
        nextpos = ((row+1)%h, col)
        if not nextpos in new_cucumbers_right and not nextpos in cucumbers_down:
            new_cucumbers_down.add(nextpos)
            changed = True
        else:
            not_moved.add(oldpos)
    for oldpos in not_moved:
        new_cucumbers_down.add(oldpos)
    return changed, new_cucumbers_right, new_cucumbers_down

def printboard(cucumbers_right, cucumbers_down, h, w):
    res = []
    for i in range(h):
        row = ""
        for j in range(w):
            if (i, j) in cucumbers_right:
                row += ">"
            elif (i, j) in cucumbers_down:
                row += "v"
            else:
                row += "."
        res.append(row)
    print("\n".join(res))
    print()

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    cucumbers_right = set()
    cucumbers_down = set()
    h, w = len(board), len(board[0])
    for row in range(h):
        for col in range(w):
            if board[row][col] == ">":
                cucumbers_right.add((row, col))
            elif board[row][col] == "v":
                cucumbers_down.add((row, col))

    t = 0
    changed = True
    while changed:
        changed, cucumbers_right, cucumbers_down = move_cucumbers(cucumbers_right, cucumbers_down, h, w)
        t += 1
    print(t)

