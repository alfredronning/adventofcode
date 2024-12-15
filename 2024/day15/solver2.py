board, moves = open("input.txt").read().strip().split("\n\n")

robot = (0, 0)
wall = set()
boxes = set()
max_x, max_y = 0, 0
for i, line in enumerate(board.split("\n")):
    max_x = max(max_x, i)
    for j, tile in enumerate(line):
        max_y = max(max_y, j)
        if tile == "#":
            wall.add((i, j*2))
            wall.add((i, j*2+1))
        elif tile == "O":
            boxes.add((i, j*2))
        elif tile == "@":
            robot = (i, j*2)

def print_board(wall, boxes, robot, x, y):
    row = ""
    for i in range(x+1):
        for j in range(0, y*2+2):
            if (i, j) in wall:
                row += "#"
            elif (i, j) in boxes:
                row += "["
            elif (i, j-1) in boxes:
                row += "]"
            elif robot == (i, j):
                row += "@"
            else:
                row += "."
        row += "\n"
    print(row)


def push_horizontal(wall, boxes, robot, d):
    push_boxes = []
    next_space = (robot[0], robot[1]+d[1])
    insideBox = d[1] == -1
    while next_space in boxes or insideBox:
        if insideBox and d[1] == -1 and (next_space[0], next_space[1]+d[1]) in wall:
            insideBox = False
            continue
        if not insideBox:
            push_boxes.append(next_space)
            insideBox = True
        else:
            insideBox = False
        next_space = (next_space[0], next_space[1]+d[1])
    if next_space in wall:
        return robot
    for box in push_boxes[::-1]:
        boxes.remove(box)
        boxes.add((box[0], box[1]+d[1]))
    return (robot[0]+d[0], robot[1]+d[1])

def push_vertical(wall, boxes, robot, d):
    push_boxes = []
    visited = set()
    queue = []
    if (robot[0]+d[0], robot[1]) in boxes:
        queue.append((robot[0]+d[0], robot[1]))
    elif (robot[0]+d[0], robot[1]-1) in boxes:
        queue.append((robot[0]+d[0], robot[1]-1))
    while queue:
        current = queue.pop()
        if current in visited:
            continue
        visited.add(current)
        push_boxes.append(current)
        if (current[0]+d[0], current[1]) in wall or (current[0]+d[0], current[1]+1) in wall:
            return robot
        if (current[0]+d[0], current[1]) in boxes:
            queue.append((current[0]+d[0], current[1]))
            continue
        if (current[0]+d[0], current[1]-1) in boxes:
            queue.append((current[0]+d[0], current[1]-1))
        if (current[0]+d[0], current[1]+1) in boxes:
            queue.append((current[0]+d[0], current[1]+1))
    for box in push_boxes[::-1]:
        boxes.remove(box)
        boxes.add((box[0]+d[0], box[1]))
    return (robot[0]+d[0], robot[1])



for move in moves:
    if move == ">":
        next = (robot[0], robot[1]+1)
        if next in boxes:
            robot = push_horizontal(wall, boxes, robot, (0, 1))
        elif next not in wall:
            robot = next
    elif move == "<":
        next = (robot[0], robot[1]-1)
        if (next[0], next[1]-1) in boxes:
            robot = push_horizontal(wall, boxes, robot, (0, -1))
        elif next not in wall:
            robot = next
    elif move == "v":
        next = (robot[0]+1, robot[1])
        if next in boxes or (next[0], next[1]-1) in boxes:
            robot = push_vertical(wall, boxes, robot, (1, 0))
        elif next not in wall:
            robot = next
    elif move == "^":
        next = (robot[0]-1, robot[1])
        if next in boxes or (next[0], next[1]-1) in boxes:
            robot = push_vertical(wall, boxes, robot, (-1, 0))
        elif next not in wall:
            robot = next
    
res = 0
for box in boxes:
    res += 100*box[0]+box[1]

print(res)

