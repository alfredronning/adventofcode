d = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def getval(inp, direction):
    inp = inp[::direction]
    for i in range(len(inp)):
        if inp[i] in "0123456789":
            return inp[i]
        if inp[i:i+3][::direction] in d:
            return d[inp[i:i+3][::direction]]
        if inp[i:i+4][::direction] in d:
            return d[inp[i:i+4][::direction]]
        if inp[i:i+5][::direction] in d:
            return d[inp[i:i+5][::direction]]
    raise Exception


if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    res = 0
    for line in inp:
        res += int(getval(line, 1) + getval(line, -1))
    print(res)

