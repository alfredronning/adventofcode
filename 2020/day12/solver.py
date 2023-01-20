FACING_DICT = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    ship_pos = [0, 0]
    facing = 0
    for instruction in instructions:
        direction, value = instruction[0], int(instruction[1:])
        if direction == "N":
            ship_pos[0] -= value
        elif direction == "S":
            ship_pos[0] += value
        elif direction == "W":
            ship_pos[1] -= value
        elif direction == "E":
            ship_pos[1] += value
        elif direction == "F":
            ship_pos[0] += FACING_DICT[facing][0]*value
            ship_pos[1] += FACING_DICT[facing][1]*value
        elif direction == "R":
            facing = (facing + value) % 360
        elif direction == "L":
            facing = (facing - value) % 360
    print(abs(ship_pos[0])+abs(ship_pos[1]))

