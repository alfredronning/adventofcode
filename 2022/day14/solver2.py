def create_rockmap(paths):
    paths = [path.split(" -> ") for path in paths]
    maxy = -float("inf")
    for path in paths:
        for pos in path:
            maxy = max(maxy, int(pos.split(",")[1]))
    minx, maxx = 500-maxy-2, 500+maxy+2
    width = maxx-minx+1
    sandpos = 500-minx
    rockmap = [["." for _ in range(width+1)] for _ in range(maxy+2)]
    for path in paths:
        for i in range(len(path)-1):
            pos0 = int(path[i].split(",")[0])-minx, int(path[i].split(",")[1])
            pos1 = int(path[i+1].split(",")[0])-minx, int(path[i+1].split(",")[1])
            for x in range(min(pos0[0], pos1[0]), max(pos0[0], pos1[0])+1):
                rockmap[pos0[1]][x] = "#"
            for y in range(min(pos0[1], pos1[1]), max(pos0[1], pos1[1])+1):
                rockmap[y][pos0[0]] = "#"
    rockmap += [["#"]*width]
    return sandpos, rockmap

def incrementpos(currentpos, rockmap):
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

def simulate(sandpos, rockmap):
    sandnr = 0
    while True:
        currentpos = [sandpos, 0]
        exitstatus = 0
        while not exitstatus:
            exitstatus, currentpos = incrementpos(currentpos, rockmap)
        if rockmap[0][sandpos] != ".":
            return sandnr
        rockmap[currentpos[1]][currentpos[0]] = "o"
        sandnr += 1

if __name__ == "__main__":
    paths = open("input.txt").read().strip().split("\n")
    print(simulate(*create_rockmap(paths)))

