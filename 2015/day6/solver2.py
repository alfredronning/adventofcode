if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    lights = [[0]*1000 for _ in range(1000)]
    for instruction in instructions:
        i_split = instruction.split()
        if i_split[0] == "toggle":
            x0, y0 = i_split[1].split(",")
            x1, y1 = i_split[3].split(",")
            for x in range(int(x0), int(x1)+1):
                for y in range(int(y0), int(y1)+1):
                    lights[x][y] += 2
        else:
            x0, y0 = i_split[2].split(",")
            x1, y1 = i_split[4].split(",")
            for x in range(int(x0), int(x1)+1):
                for y in range(int(y0), int(y1)+1):
                    lights[x][y] = lights[x][y] + 1 if i_split[1] == "on" else max(0, lights[x][y]-1)
    count = 0
    for x in range(1000):
        for y in range(1000):
            count += lights[x][y]
    print(count)

