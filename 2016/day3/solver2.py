if __name__ == "__main__":
    triangles = [[int(side) for side in sides.split()] for sides in open("input.txt").read().strip().split("\n")]
    count = 0
    for i in range(len(triangles)*len(triangles[0])//3):
        sides = []
        for j in range(3):
            pos = i*3+j
            y, x = divmod(pos, len(triangles))
            sides.append(triangles[x][y])
        print(sides)
        if max(sides)*2 < sum(sides):
            count += 1
    print(count)

