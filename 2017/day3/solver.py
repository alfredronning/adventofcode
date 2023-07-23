from math import exp


def swap_direction(bounds, pos, direction):
    x, y = pos[0]+direction[0], pos[1]+direction[1]
    return x < -bounds or x > bounds or y < -bounds or y > bounds

if __name__ == "__main__":
    inp = 277678
    grid = {}

    pos = (0, 0)
    bounds = 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    current_direction = 0
    expanded = False

    for _ in range(inp-1):
        if swap_direction(bounds, pos, directions[current_direction]):
            if current_direction == 0 and not expanded:
                bounds += 1
                expanded = True
            else:
                current_direction = (current_direction + 1) % len(directions)
                expanded = False
        pos = (pos[0] + directions[current_direction][0], pos[1] + directions[current_direction][1])
    print(abs(pos[0]) + abs(pos[1]))

