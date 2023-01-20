if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    ship_pos = [0, 0]
    waypoint = [-1, 10]
    for instruction in instructions:
        direction, value = instruction[0], int(instruction[1:])
        if direction == "N":
            waypoint[0] -= value
        elif direction == "S":
            waypoint[0] += value
        elif direction == "W":
            waypoint[1] -= value
        elif direction == "E":
            waypoint[1] += value
        elif direction == "F":
            ship_pos[0] += waypoint[0]*value
            ship_pos[1] += waypoint[1]*value
        elif direction == "R":
            if value == 90:
                waypoint = [waypoint[1], -waypoint[0]]
            if value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if value == 270:
                waypoint = [-waypoint[1], waypoint[0]]
        elif direction == "L":
            if value == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            if value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if value == 270:
                waypoint = [waypoint[1], -waypoint[0]]
    print(abs(ship_pos[0])+abs(ship_pos[1]))

