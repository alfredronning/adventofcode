robots = open("input.txt").read().strip().split("\n")

def parse_robot(r):
    r = r.split("p=")[1]
    p, v = r.split(" v=")
    return (tuple(int(i) for i in p.split(",")), tuple(int(i) for i in v.split(",")))

def move_robot(r, time, mx, my):
    return ((r[0][0]+r[1][0]*time)%mx, (r[0][1]+r[1][1]*time)%my)

time = 100
width = 101
height = 103
robots = [parse_robot(r) for r in robots]
robots = [move_robot(r, time, width, height) for r in robots]

first = len([r for r in robots if (r[0] < width // 2) and (r[1] < height // 2)])
second = len([r for r in robots if (r[0] < width // 2) and (r[1] > height // 2)])
third = len([r for r in robots if (r[0] > width // 2) and (r[1] < height // 2)])
fourth = len([r for r in robots if (r[0] > width // 2) and (r[1] > height // 2)])

print(first*second*third*fourth)

