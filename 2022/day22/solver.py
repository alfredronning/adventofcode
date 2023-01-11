import re

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def on_board(board, pos):
    try:
        return board[pos[0]][pos[1]] != " "
    except IndexError:
        return False

def find_wrap(board, pos, direction):
    newposx = pos[0]%len(board) if direction[0] else pos[0]
    newposy = pos[1]%len(board[pos[0]]) if direction[1] else pos[1]
    pos = newposx, newposy
    while not on_board(board, pos):
        newposx = (pos[0] + direction[0])%len(board) if direction[0] else pos[0]
        newposy = (pos[1] + direction[1])%len(board[pos[0]]) if direction[1] else pos[1]
        pos = newposx, newposy
    return pos

def move(board, pos, direction, length):
    for _ in range(length):
        newpos = pos[0]+direction[0], pos[1]+direction[1]
        if on_board(board, newpos):
            if board[newpos[0]][newpos[1]] == "#":
                break
            pos = newpos
        else:
            newpos = find_wrap(board, newpos, direction)
            if board[newpos[0]][newpos[1]] == "#":
                break
            pos = newpos
    return pos

if __name__ == "__main__":
    board, path = open("input.txt").read().split("\n\n")
    board = board.split("\n")
    path = [int(i) if i.isdigit() else i for i in re.split('(\d+)', path.strip()) if i]

    pos = 0, board[0].index(".")
    facing = 0
    for i, instruction in enumerate(path):
        if type(instruction) == int:
            pos = move(board, pos, DIRECTIONS[facing], instruction)
        else:
            if instruction == "R":
                facing = (facing+1)%4
            else:
                facing = (facing-1)%4
    print(1000*(pos[0]+1) + 4*(pos[1]+1) + facing)
