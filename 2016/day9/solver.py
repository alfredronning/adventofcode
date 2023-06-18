def calc_sequence(a, b, inp):
    res = ""
    for _ in range(b):
        res += inp[:a]
    return res

def calc_decompressed(inp):
    res = ""
    i = 0
    while i < len(inp):
        if inp[i] != "(":
            res += inp[i]
            i += 1
        else:
            i += 1
            a = ""
            while inp[i] != "x":
                a += inp[i]
                i += 1
            i += 1
            b = ""
            while inp[i] != ")":
                b += inp[i]
                i += 1
            i += 1
            res += calc_sequence(int(a), int(b), inp[i:])
            i += int(a)
    return res 

if __name__ == "__main__":
    inputs = open("input.txt").read().strip().split("\n")
    size = 0
    for inp in inputs:
        size += len(calc_decompressed(inp))
    print(size)

