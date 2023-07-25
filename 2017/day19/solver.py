def travel_route(path):
    pos = (0, path[0].index("|"))
    direction = (1, 0)
    route = ""
    steps = 0

    while True:
        steps += 1
        pos = (pos[0]+direction[0], pos[1]+direction[1])
        if path[pos[0]][pos[1]] == " ":
            return route, steps
        if path[pos[0]][pos[1]].isalpha():
            route += path[pos[0]][pos[1]]
        if path[pos[0]][pos[1]] == "+":
            for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if d[0] == -direction[0] and d[1] == -direction[1]:
                    continue
                n = (pos[0]+d[0], pos[1]+d[1])
                if n[0] < 0 or n[0] >= len(path) or n[1] < 0 or n[1] >= len(path[0]):
                    continue
                if path[n[0]][n[1]].isalpha() or path[n[0]][n[1]] in "-|":
                    direction = d
                    break


if __name__ == "__main__":
    path = [[c for c in row] for row in open("input.txt").read().split("\n")]
    print(travel_route(path))

