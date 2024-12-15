board, moves = open("input.txt").read().strip().split("\n\n")

D = {
    "v": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1)
}

robot = (0, 0)
wall = set()
boxes = set()
max_x, maxy = 0, 0
for i, line in enumerate(board.split("\n")):
    for j, tile in enumerate(line):
        if tile == "#":
            wall.add((i, j))
        elif tile == "O":
            boxes.add((i, j))
        elif tile == "@":
            robot = (i, j)

def print_board(wall, boxes, robot, x, y):
    row = ""
    for i in range(x):
        for j in range(y):
            if (i, j) in wall:
                row += "#"
            elif (i, j) in boxes:
                row += "O"
            elif robot == (i, j):
                row += "@"
            else:
                row += "."
        row += "\n"
    print(row)


def push(wall, boxes, robot, d):
    push_boxes = []
    next_space = (robot[0]+d[0], robot[1]+d[1])
    while next_space in boxes:
        push_boxes.append(next_space)
        next_space = (next_space[0]+d[0], next_space[1]+d[1])
    if next_space in wall:
        return robot
    for box in push_boxes[::-1]:
        boxes.remove(box)
        boxes.add((box[0]+d[0], box[1]+d[1]))
    return (robot[0]+d[0], robot[1]+d[1])



for move in moves:
    if move not in D:
        continue
    d = D[move]
    next = (robot[0]+d[0], robot[1] + d[1])
    if next in boxes:
        robot = push(wall, boxes, robot, d)
    elif next not in wall:
        robot = next
    #print_board(wall, boxes, robot, 8, 8)

res = 0
for box in boxes:
    res += 100*box[0]+box[1]

print(res)

