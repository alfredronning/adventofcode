if __name__ == "__main__":
    instructions = [i.split() for i in open("input.txt").read().strip().split("\n")]
    cycle = 0
    x = 1
    signal_strength = 0
    for instruction in instructions:
        cycle += 1
        if (cycle-20)%40 == 0:
            signal_strength += cycle*x
        if instruction[0] == "addx":
            cycle += 1
            if (cycle-20)%40 == 0:
                signal_strength += cycle*x
            x += int(instruction[1])
    print(signal_strength)

