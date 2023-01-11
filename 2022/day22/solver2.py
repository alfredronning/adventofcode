import re

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def on_board(board, pos):
    try:
        return pos[0] >= 0 and pos[1] >= 0 and board[pos[0]][pos[1]] != " "
    except IndexError:
        return False

def find_wrap(facing, pos):
    if pos[0] == 200:
        return 1, (0, pos[1]+100)
    if pos[0] == -1:
        if pos[1] < 100:
            return 0, (pos[1]+100, 0)
        return 3, (199, pos[1]-100)
    if pos[1] == 150:
        return 2, (149-pos[0], 99)
    if pos[1] == -1:
        if pos[0] < 150:
            return 0, (149-pos[0], 50)
        return 1, (0, pos[0]-100)
    if pos[1] < 50:
        if facing == 3:
            return 0, (50+pos[1], 50)
        if pos[0] < 50:
            return 0, (149-pos[0], 0)
        return 1, (100, pos[0]-50)
    if pos[0] >= 150:
        if facing == 0:
            return 3, (149, pos[0]-100)
        return 2, (pos[1]+100, 49)
    if pos[1] >= 100:
        if facing == 1:
            return 2, (pos[1]-50, 99)
        if pos[0] < 100:
            return 3, (49, pos[0]+50)
        return 2, (149-pos[0], 149)
    raise Exception("No wrap for: "+str(pos))

def move(board, pos, facing, length, i):
    for _ in range(length):
        direction = DIRECTIONS[facing]
        newpos = pos[0]+direction[0], pos[1]+direction[1]
        if on_board(board, newpos):
            if board[newpos[0]][newpos[1]] == "#":
                break
            pos = newpos
        else:
            newfacing, newpos = find_wrap(facing, newpos)
            if board[newpos[0]][newpos[1]] == "#":
                break
            facing, pos = newfacing, newpos
    return facing, pos

if __name__ == "__main__":
    board, path = open("input.txt").read().split("\n\n")
    board = board.split("\n")
    path = [int(i) if i.isdigit() else i for i in re.split('(\d+)', path.strip()) if i]

    pos = 0, board[0].index(".")
    facing = 0
    for i, instruction in enumerate(path):
        if type(instruction) == int:
            facing, pos = move(board, pos, facing, instruction, i)
        else:
            if instruction == "R":
                facing = (facing+1) % 4
            else:
                facing = (facing-1) % 4
    print(1000*(pos[0]+1) + 4*(pos[1]+1) + facing)

