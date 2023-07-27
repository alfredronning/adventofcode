if __name__ == "__main__":
    depth = 3558
    target = (15,740)
    m = 20183

    e = dict()
    for x in range(0, target[0]+1):
        for y in range(0, target[1]+1):
            if (x, y) == target:
                g = 0
            elif x == 0:
                g = y*48271
            elif y == 0:
                g = x*16807
            else:
                g = (e[(x-1, y)]*e[(x, y-1)])
            e[(x, y)] = (g+depth)%m
    print(sum(r%3 for r in e.values()))

