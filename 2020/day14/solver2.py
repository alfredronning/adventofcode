import re
from collections import defaultdict

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    bitmask = 0
    bitmask_negative = 0

    memdict = defaultdict(lambda: "0"*36)
    for instruction in instructions:
        if instruction[:4] == "mask":
            bitmask = instruction.split("mask = ")[1]
        else:
            mem, val = [int(i) for i in re.findall(r"mem\[(\d*)\] = (\d*)", instruction)[0]]
            mem_bin = "{:036b}".format(mem)
            splits = [""]
            currentseg = ""
            for i, bit in enumerate(bitmask):
                if bit == "0":
                    currentseg += mem_bin[i]
                elif bit == "1":
                    currentseg += "1"
                else:
                    for _ in range(len(splits)):
                        s = splits.pop(0)
                        splits.append(s+currentseg+"0")
                        splits.append(s+currentseg+"1")
                    currentseg = ""
            for s in splits:
                memdict[int(s+currentseg, 2)] = val
    print(sum(memdict.values()))

