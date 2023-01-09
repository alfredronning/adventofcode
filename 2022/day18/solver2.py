if __name__ == "__main__":
    cubes = set(tuple(int(i) for i in line.split(",")) for line in open("input.txt").read().strip().split("\n"))
    min_v = min(min(cube) for cube in cubes)-1
    max_v = max(max(cube) for cube in cubes)+1

    surface_area = 0
    queue = [(0, 0, 0)]
    visited = set()
    while queue:
        x, y, z = queue.pop(0)
        visited.add((x, y, z))
        for dx, dy, dz in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            neighbour = (x+dx, y+dy, z+dz) 
            if min(neighbour) < min_v or max(neighbour) > max_v:
                continue
            if neighbour not in visited and neighbour not in queue:
                if neighbour in cubes:
                    surface_area += 1
                else:
                    queue.append(neighbour)
    print(surface_area)

