if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    res = ""
    pos = [1, 1]
    for instruction in instructions:
        for direction in instruction:
            if direction == "U" and pos[0] > 0:
                pos[0] -= 1
            elif direction == "D" and pos[0] < 2:
                pos[0] += 1
            elif direction == "L" and pos[1] > 0:
                pos[1] -= 1
            elif direction == "R" and pos[1] < 2:
                pos[1] += 1
        res += str(pos[0]*3+pos[1]+1)
    print(res)

