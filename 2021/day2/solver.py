if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    pos = [0, 0]
    for instruction in instructions:
        direction, length = instruction.split()
        if direction == "forward":
            pos[1] += int(length)
        if direction == "down":
            pos[0] += int(length)
        if direction == "up":
            pos[0] -= int(length)
    print(pos[0]*pos[1])

