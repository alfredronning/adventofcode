import re

inp = open("input.txt").read().strip()

mults = re.findall(r'mul\(\d+,\d+\)', inp)

res = 0
for mul in mults:
    d1, d2 = mul[4:-1].split(",")
    res += int(d1) * int(d2)

print(res)
