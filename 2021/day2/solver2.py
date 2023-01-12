if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    pos = [0, 0]
    aim = 0
    for instruction in instructions:
        direction, length = instruction.split()
        if direction == "forward":
            pos[1] += int(length)
            pos[0] += int(length) * aim
        if direction == "down":
            aim += int(length)
        if direction == "up":
            aim -= int(length)
    print(pos[0]*pos[1])

