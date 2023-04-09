from math import atan2, pi

def visible(astriods, pos1, pos2):
    d_x = pos2[0] - pos1[0]
    d_y = pos2[1] - pos1[1]
    steps = 0
    if d_x == 0:
        direction = 1 if pos1[1] < pos2[1] else -1
        while steps < abs(d_y) - 1:
            steps += 1
            if astriods[pos1[0]][pos1[1]+steps*direction] == "#":
                return False
    if d_y == 0:
        direction = 1 if pos1[0] < pos2[0] else -1
        while steps < abs(d_x) - 1:
            steps += 1
            if astriods[pos1[0]+steps*direction][pos1[1]] == "#":
                return False
    else:
        direction = 1 if pos1[0] < pos2[0] else -1
        while steps < abs(d_x) - 1:
            steps += 1
            y_step = steps*d_y/d_x*direction
            if int(y_step) == y_step:
                if astriods[pos1[0]+steps*direction][pos1[1]+int(y_step)] == "#":
                    return False
    return True


def count_astriods(astriods, pos):
    count = 0
    for i, row in enumerate(astriods):
        for j, tile in enumerate(row):
            if astriods[i][j] == "." or pos == (i, j):
                continue
            count += visible(astriods, pos, (i, j))
    return count

if __name__ == "__main__":
    astriods = open("input.txt").read().strip().split("\n")
    best_count = 0
    best_station = (0, 0)
    for i, row in enumerate(astriods):
        for j, tile in enumerate(row):
            if astriods[i][j] == "#":
                current_count = count_astriods(astriods, (i, j))
                if current_count > best_count:
                    best_count = current_count
                    best_station = (i, j)
    slope_dict = {}
    for i, row in enumerate(astriods):
        for j, tile in enumerate(row):
            if astriods[i][j] == "." or (i, j) == best_station:
                continue
            d_x = best_station[0]-i
            d_y = j-best_station[1]
            if d_x == 0:
                angle = 0
            else:
                angle = atan2(d_y, d_x)
                if angle < 0:
                    angle += 2*pi
            if angle in slope_dict:
                old = slope_dict[angle]
                if d_y**2+d_x**2 < (old[0]-best_station[0])**2+(old[1]-best_station[1])**2:
                    slope_dict[angle] = (i, j)
            else:
                slope_dict[angle] = (i, j)
    angles = sorted(slope_dict.keys())
    y, x = slope_dict[angles[200-1]]
    print(x*100+y+1)
