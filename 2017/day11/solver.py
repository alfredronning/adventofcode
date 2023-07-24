if __name__ == "__main__":
    steps = open("input.txt").read().strip().split(",")

    pos = [0.0, 0.0]
    max_steps = 0

    for step in steps:
        if step == "n":
            pos[0] -= 1
        if step == "s":
            pos[0] += 1
        if step == "nw":
            pos[0] -= .5
            pos[1] -= .5
        if step == "ne":
            pos[0] -= .5
            pos[1] += .5
        if step == "sw":
            pos[0] += .5
            pos[1] -= .5
        if step == "se":
            pos[0] += .5
            pos[1] += .5
        max_steps = max(max_steps, abs(pos[0])+abs(pos[1]))

    print(abs(pos[0])+abs(pos[1]))
    print(max_steps)

