def create_rockmap(paths):
    paths = [path.split(" -> ") for path in paths]
    minx, maxx = float("inf"), -float("inf")
    maxy = -float("inf")
    for path in paths:
        for pos in path:
            xpos = int(pos.split(",")[0])
            ypos = int(pos.split(",")[1])
            minx = min(minx, xpos)
            maxx = max(maxx, xpos)
            maxy = max(maxy, ypos)
    width = maxx-minx+1
    sandpos = 500-minx
    rockmap = [["." for _ in range(width+1)] for _ in range(maxy+1)]
    for path in paths:
        for i in range(len(path)-1):
            pos0 = int(path[i].split(",")[0])-minx, int(path[i].split(",")[1])
            pos1 = int(path[i+1].split(",")[0])-minx, int(path[i+1].split(",")[1])
            for x in range(min(pos0[0], pos1[0]), max(pos0[0], pos1[0])+1):
                rockmap[pos0[1]][x] = "#"
            for y in range(min(pos0[1], pos1[1]), max(pos0[1], pos1[1])+1):
                rockmap[y][pos0[0]] = "#"
    return sandpos, rockmap

def incrementpos(currentpos, rockmap):
    try:
        if rockmap[currentpos[1]+1][currentpos[0]] == ".":
            currentpos[1] += 1
        elif rockmap[currentpos[1]+1][currentpos[0]-1] == ".":
            currentpos[1] += 1
            currentpos[0] -= 1
        elif rockmap[currentpos[1]+1][currentpos[0]+1] == ".":
            currentpos[1] += 1
            currentpos[0] += 1
        else:
            return 1, currentpos
        return 0, currentpos
    except Exception:
        return 2, currentpos
    
def simulate(sandpos, rockmap):
    sandnr = 0
    while True:
        currentpos = [sandpos, 0]
        exitstatus = 0
        while not exitstatus:
            exitstatus, currentpos = incrementpos(currentpos, rockmap)
        if exitstatus == 2:
            return sandnr
        rockmap[currentpos[1]][currentpos[0]] = "o"
        sandnr += 1

if __name__ == "__main__":
    paths = open("input.txt").read().strip().split("\n")
    print(simulate(*create_rockmap(paths)))

