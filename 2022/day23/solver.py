DIRECTIONS = {
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, 1), 
    "W": (0, -1),
    "E": (0, 1),
    "SW": (1, -1),
    "S": (1, 0),
    "SE": (1, 1)
}

COVER_DIRECTIONS = [
    ("NW", "N", "NE"),
    ("SW", "S", "SE"),
    ("NW", "W", "SW"),
    ("NE", "E", "SE")
]

MOVE = [
    lambda x: (x[0]-1, x[1]),
    lambda x: (x[0]+1, x[1]),
    lambda x: (x[0], x[1]-1),
    lambda x: (x[0], x[1]+1)
]

def can_move(elves_pos, elf, cover_direction):
    for cover in cover_direction:
        neighbour = elf[0]+DIRECTIONS[cover][0], elf[1]+DIRECTIONS[cover][1]
        if neighbour in elves_pos:
            return False
    return True

def move_elves(elves_pos, i):
    movedict = {}
    for elf in elves_pos:
        legal = [can_move(elves_pos, elf, cover_direction) for cover_direction in COVER_DIRECTIONS]
        if sum(legal) == 0 or sum(legal) == 4:
            continue
        elif legal[i % 4]:
            movedict[elf] = MOVE[i % 4](elf)
        elif legal[(i+1) % 4]:
            movedict[elf] = MOVE[(i+1) % 4](elf)
        elif legal[(i+2) % 4]:
            movedict[elf] = MOVE[(i+2) % 4](elf)
        elif legal[(i+3) % 4]:
            movedict[elf] = MOVE[(i+3) % 4](elf)
    for elf in movedict:
        if list(movedict.values()).count(movedict[elf]) == 1:
            elves_pos.remove(elf)
            elves_pos.add(movedict[elf])

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    elves_pos = set()
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == "#":
                elves_pos.add((i, j))
    for i in range(10):
        move_elves(elves_pos, i)
    minx = miny = float("inf")
    maxx = maxy = -float("inf")
    for elf in elves_pos:
        minx = min(minx, elf[0])
        maxx = max(maxx, elf[0])
        miny = min(miny, elf[1])
        maxy = max(maxy, elf[1])
    print((maxx+1-minx)*(maxy+1-miny)-len(elves_pos))
