def simulate_end(init, bots_holding, bots_split, outputs):
    chip_number, to = init
    holding = bots_holding[to]
    if holding is None:
        bots_holding[to] = chip_number
    else:
        low, high = bots_split[to]
        chips = sorted([chip_number, holding])
        bots_holding[to] = None
        if low[0] == "output":
            outputs[int(low[1])] = chips[0]
        else:
            simulate_end([chips[0], int(low[1])], bots_holding, bots_split, outputs)
        if high[0] == "output":
            outputs[int(high[1])] = chips[1]
        else:
            simulate_end([chips[1], int(high[1])], bots_holding, bots_split, outputs)

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    goesto = []
    bots_split = {}
    bots_holding = {}
    for instruction in instructions:
        if "value" in instruction:
            goesto.append([int(i) for i in instruction.split("value ")[1].split(" goes to bot ")])
        else:
            splits = instruction.split()
            bots_split[int(splits[1])] = [splits[5:7], splits[10:12]]
            bots_holding[int(splits[1])] = None

    outputs = {}
    for init in goesto:
        simulate_end(init, bots_holding, bots_split, outputs)
    res = 1
    for i in range(3):
        res *= outputs[i]
    print(res)

