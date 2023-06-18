def simulate_end(init, bots_holding, bots_split):
    chip_number, to = init
    holding = bots_holding[to]
    if holding is None:
        bots_holding[to] = chip_number
    else:
        low, high = bots_split[to]
        chips = sorted([chip_number, holding])
        bots_holding[to] = None
        if chips == [17, 61]:
            print(to)
        simulate_end([chips[0], low], bots_holding, bots_split)
        simulate_end([chips[1], high], bots_holding, bots_split)


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
            bots_split[int(splits[1])] = [int(splits[6]), int(splits[11])]
            bots_holding[int(splits[1])] = None

    for init in goesto:
        simulate_end(init, bots_holding, bots_split)
    print(bots_holding)

