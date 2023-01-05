if __name__ == "__main__":
    instructions = [i.split() for i in open("input.txt").read().strip().split("\n")]
    cycle = 0
    x = 1
    crt = ""
    for instruction in instructions:
        crt += "#" if abs(cycle%40-x) <= 1 else "."
        cycle += 1
        if instruction[0] == "addx":
            crt += "#" if abs(cycle%40-x) <= 1 else "."
            cycle += 1
            x += int(instruction[1])
    print("\n".join(crt[i*40: i*40+40] for i in range(len(crt)//40)))

