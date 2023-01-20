def find_min_max(active_cubes):
    minx = miny = minz = minw = float("inf")
    maxx = maxy = maxz = maxw = -float("inf")
    for cube in active_cubes:
        minx = min(minx, cube[0])
        miny = min(miny, cube[1])
        minz = min(minz, cube[2])
        minw = min(minw, cube[3])
        maxx = max(maxx, cube[0])
        maxy = max(maxy, cube[1])
        maxz = max(maxz, cube[2])
        maxw = max(maxw, cube[3])
    return minx-1, miny-1, minz-1, minw-1, maxx+2, maxy+2, maxz+2, maxw+2

def count_active_neighbours(active_cubes, current_cube):
    neighbour_set = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    neighbour = (current_cube[0]+dx, current_cube[1]+dy, current_cube[2]+dz, current_cube[3]+dw)
                    if neighbour == current_cube:
                        continue
                    if neighbour in active_cubes:
                        neighbour_set.add(neighbour)
    return len(neighbour_set)
    
def simulate_round(active_cubes):
    minx, miny, minz, minw, maxx, maxy, maxz, maxw = find_min_max(active_cubes)
    new_active = set()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            for z in range(minz, maxz):
                for w in range(minw, maxw):
                    current_cube = (x, y, z, w)
                    active_neighbours = count_active_neighbours(active_cubes, current_cube)
                    if current_cube in active_cubes and active_neighbours in [2, 3]:
                        new_active.add(current_cube)
                    if current_cube not in active_cubes and active_neighbours == 3:
                        new_active.add(current_cube)
    return new_active

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    active_cubes = set()
    for i, row in enumerate(board):
        for j, cube in enumerate(row):
            if cube == "#":
                active_cubes.add((i, j, 0, 0))
    for _ in range(6):
        active_cubes = simulate_round(active_cubes)
    print(len(active_cubes))

