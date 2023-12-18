if __name__ == "__main__":
    dig = [i.split() for i in open("input.txt").read().strip().split("\n")]
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    current = (0, 0)
    points = [current]
    res = 0
    for d, l, _ in dig:
        l = int(l)
        res += l
        end = (current[0]+directions[d][0]*l, current[1]+directions[d][1]*l)
        current = end
        points.append(current)

    res2 = 0
    for i in range(len(points)-1):
        res2 += points[i][0]*points[i+1][1]
        res2 -= points[i][1]*points[i+1][0]
    print(int(0.5*(abs(res2)+res)+1))

