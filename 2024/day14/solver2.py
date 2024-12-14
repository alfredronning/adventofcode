robots = open("input.txt").read().strip().split("\n")
l = len(robots)

def parse_robot(r):
    r = r.split("p=")[1]
    p, v = r.split(" v=")
    return (tuple(int(i) for i in p.split(",")), tuple(int(i) for i in v.split(",")))

def move_robot(r, time, mx, my):
    return (((r[0][0]+r[1][0]*time)%mx, (r[0][1]+r[1][1]*time)%my), r[1])

def print_robots(p, height, width):
    board = ""
    for i in range(height):
        for j in range(width):
            if (i, j) in p:
                board += "#"
            else:
                board += " "
        board += "\n"
    print(board)


width = 101
height = 103
robots = [parse_robot(r) for r in robots]

time = 0
while True:
    time += 1
    robots = [move_robot(r, 1, width, height) for r in robots]
    pos = set(r[0] for r in robots)
    if len(pos) == l:
        print(time)
        print_robots(pos, height, width)
        break


