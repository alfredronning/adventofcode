if __name__ == "__main__":
    space = open("input.txt").read().strip().split("\n")
    empty_row = [True]*len(space)
    empty_col = [True]*len(space[0])
    planets = []
    planet_idx = 0
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == "#":
                empty_row[i] = False
                empty_col[j] = False
                planets.append((i, j))
    empty_row = [sum(empty_row[:i]) for i in range(len(empty_row))]
    empty_col = [sum(empty_col[:i]) for i in range(len(empty_col))]
    space_expansion = 1000000-1
    for i in range(len(planets)):
        x, y = planets[i]
        planets[i] = (x + empty_row[x]*space_expansion, y + empty_col[y]*space_expansion)
    res = 0
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            res += abs(planets[i][0]-planets[j][0])+abs(planets[i][1]-planets[j][1])
    print(res)

