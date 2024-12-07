inp = open("input.txt").read().strip().split("\n")

l1 = sorted(int(l.split("  ")[0]) for l in inp)
l2 = sorted(int(l.split("  ")[1]) for l in inp)

counts = {}

for n in l2:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
res = 0
for n in l1:
    if n not in counts:
        continue
    res += n*counts[n]
print(res)
