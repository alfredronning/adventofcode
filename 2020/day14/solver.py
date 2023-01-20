import re

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    bitmask = 0
    bitmask_negative = 0

    memdict = dict()
    for instruction in instructions:
        if instruction[:4] == "mask":
            bitmask = int("".join(x if x == "1" else "0" for x in instruction.split("mask = ")[1]), 2)
            bitmask_negative = int("".join(x if x == "0" else "1" for x in instruction.split("mask = ")[1]), 2)
        else:
            mem, val = [int(i) for i in re.findall(r"mem\[(\d*)\] = (\d*)", instruction)[0]]
            val &= bitmask_negative
            val |= bitmask
            memdict[mem] = int(val)
    print(sum(memdict.values()))

