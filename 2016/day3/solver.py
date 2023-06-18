if __name__ == "__main__":
    triangles = open("input.txt").read().strip().split("\n")
    count = 0
    for triangle in triangles:
        sides = [int(side) for side in triangle.split()]
        if max(sides)*2 < sum(sides):
            count += 1
    print(count)
        
