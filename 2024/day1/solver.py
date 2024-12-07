inp = open("input.txt").read().strip().split("\n")

l1 = sorted(int(l.split("  ")[0]) for l in inp)
l2 = sorted(int(l.split("  ")[1]) for l in inp)

res = 0
for i in range(len(l1)):
    res += abs(l1[i]-l2[i])
print(res)

