def safe(report):
    increasing = None
    prev = report[0]
    for n in report[1:]:
        if increasing is None:
            increasing = True if n > prev else False
        else:
            if (increasing and n < prev) or (not increasing and n > prev):
                return False
        diff = abs(n-prev)
        if diff >= 1 and diff <= 3:
            prev = n
            continue
        return False
    return True


inp = open("input.txt").read().strip().split("\n")

res = sum(safe([int(i) for i in l.split()]) for l in inp)
print(res)

