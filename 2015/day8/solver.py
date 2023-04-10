def count_inp(inp):
    res = 2
    i = 0
    while i < len(inp)-1:
        if inp[i] == "\\":
            if inp[i+1] == "x":
                res += 3
                i += 3
            else:
                res += 1
                i += 1
        i += 1
    return res

if __name__ == "__main__":
    inputs = open("input.txt").read().strip().split("\n")
    res = 0
    for inp in inputs:
        res += count_inp(inp)
    print(res)

