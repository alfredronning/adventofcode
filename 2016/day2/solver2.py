def is_inside(pos):
    if pos[0] < 0 or pos[0] > 4:
        return False
    if pos[0] == 0 or pos[0] == 4:
        if pos[1] != 2:
            return False
    if pos[0] == 1 or pos[0] == 3:
        if pos[1] < 1 or pos[1] > 3:
            return False
    if pos[0] == 2:
        if pos[1] < 0 or pos[1] > 4:
            return False
    return True

VALUE_DICT = {
    (0, 2): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "4",
    (2, 0): "5",
    (2, 1): "6",
    (2, 2): "7",
    (2, 3): "8",
    (2, 4): "9",
    (3, 1): "A",
    (3, 2): "B",
    (3, 3): "C",
    (3, 2): "D",
}

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    res = ""
    pos = [1, 1]
    for instruction in instructions:
        for direction in instruction:
            if direction == "U" and is_inside((pos[0]-1, pos[1])):
                pos[0] -= 1
            elif direction == "D" and is_inside((pos[0]+1, pos[1])):
                pos[0] += 1
            elif direction == "L" and is_inside((pos[0], pos[1]-1)):
                pos[1] -= 1
            elif direction == "R" and is_inside((pos[0], pos[1]+1)):
                pos[1] += 1
        res += VALUE_DICT[(pos[0], pos[1])]
    print(res)

