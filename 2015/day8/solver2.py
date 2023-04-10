def count_inp(inp):
    res = inp.count("\"") + inp.count("\\") + 2
    return res

if __name__ == "__main__":
    inputs = open("input.txt").read().strip().split("\n")
    res = 0
    for inp in inputs:
        res += count_inp(inp)
    print(res)

