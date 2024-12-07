import re

inp = open("input.txt").read().strip()

def apply_mults(s):
    mults = re.findall(r'mul\(\d+,\d+\)', s)

    res = 0
    for mul in mults:
        d1, d2 = mul[4:-1].split(",")
        res += int(d1) * int(d2)
    return res

dos = [m.start() for m in re.finditer(r'do\(\)', inp)]
donts = [m.start() for m in re.finditer(r'don\'t()', inp)] + [len(inp)]

res = 0
start_idx = 0
do = True
while len(dos) or len(donts):
    min_do = float("inf") if not len(dos) else dos[0]
    min_dont = float("inf") if not len(donts) else donts[0]
    if min_do < min_dont:
        if do is not True:
            start_idx = min_do
        do = True
        dos = dos[1:]
    else:
        if do is True:
            res += apply_mults(inp[start_idx:min_dont])
        do = False
        donts = donts[1:]

print(res)
