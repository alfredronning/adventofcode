def bounded(clay_spots, bounded_set, pos):
    left_pos = pos
    while left_pos not in clay_spots:
        if (left_pos[0]+1, left_pos[1]) not in clay_spots and (left_pos[0]+1, left_pos[1]) not in bounded_set:
            return False
        left_pos = (left_pos[0], left_pos[1]-1)
    right_pos = pos
    while right_pos not in clay_spots:
        if (right_pos[0]+1, right_pos[1]) not in clay_spots and (right_pos[0]+1, right_pos[1]) not in bounded_set:
            return False
        right_pos = (right_pos[0], right_pos[1]+1)
    return True


def print_board(clay_spots, visited, bounded_set, water):
    print("-------------------------------------------------------")
    min_y = 100000000
    max_x = max_y = 0
    for spot in visited:
        if spot in visited or spot in bounded_set:
            min_y = min(min_y, spot[1]-1)
            max_x = max(max_x, spot[0]+1)
            max_y = max(max_y, spot[1]+1)
    for i in range(0, max_x+1):
        row = ""
        for j in range(min_y, max_y+1):
            if (i, j) in bounded_set:
                row += "~"
            elif (i, j) in clay_spots:
                row += "#"
            elif (i, j) in visited:
                row += "|"
            elif (i, j) == water:
                row += "+"
            else:
                row += "."
        print(row)
    print("-------------------------------------------------------")
    print()
    print()
    print()
    print()
    print()

    
def simulate(clay_spots, water, max_x):
    visited = set()
    bounded_set = set()
    down_set = set()
    queue = [(1, water[1])]
    while queue:
        queue.sort()
        x, y = queue.pop()
        if (x, y) in visited:
            continue
        if x > max_x:
            continue
        visited.add((x, y))
        down = (x+1, y)
        if down not in clay_spots and down not in visited:
            queue.append(down) # type: ignore
            down_set.add(down)
            continue
        if down in visited and down not in bounded_set:
            continue
        tile_bounded = bounded(clay_spots, bounded_set, (x, y))
        for dy in [-1, 1]:
            left_right = (x, y+dy)
            if left_right in clay_spots:
                continue
            if left_right in visited:
                if tile_bounded and left_right not in bounded_set:
                    queue.append(left_right)
                    visited.remove(left_right)
                continue
            queue.append(left_right)
        if tile_bounded:
            bounded_set.add((x, y)) 
        if (x, y) in down_set and tile_bounded:
            queue.append((x-1, y)) # type: ignore
            visited.remove((x-1, y))
    print_board(clay_spots, visited, bounded_set, water)
    return len(visited), len(bounded_set)

if __name__ == "__main__":
    veins = open("input.txt").read().strip().split("\n")
    clay_spots = set()
    water = (0, 500)
    max_x = 0
    for vein in veins:
        first, second = vein.split(", ")
        first_coord, first_val = first.split("=")
        second_coord, second_val = second.split("=")
        first_val = int(first_val)
        second_val = [int(i) for i in second_val.split("..")]
        for i in range(second_val[0], second_val[1]+1):
            clay_spot = (i, first_val) if first_coord == "x" else (first_val, i)
            clay_spots.add(clay_spot)
            max_x = max(max_x, clay_spot[0])

    print(simulate(clay_spots, water, max_x))

