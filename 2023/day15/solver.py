def calc_hash(s):
    current = 0
    for c in s:
        o = ord(c)
        current += o
        current *= 17
        current &= 0b11111111
    return current

if __name__ == "__main__":
    steps = open("input.txt").read().strip().split(",")
    res = 0
    for step in steps:
        res += calc_hash(step)
    print(res)

