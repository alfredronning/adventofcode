if __name__ == "__main__":
    cubes = set(tuple(int(i) for i in line.split(",")) for line in open("input.txt").read().strip().split("\n"))
    surface_area = 0
    for x, y, z in cubes:
        for dx, dy, dz in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            neighbour = (x+dx, y+dy, z+dz) 
            if not neighbour in cubes:
                surface_area += 1
    print(surface_area)

