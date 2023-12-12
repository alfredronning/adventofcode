def is_valid(springs, counts):
    groups = [g for g in springs.split(".") if g]
    if len(groups) != len(counts):
        return False
    for i in range(len(counts)):
        if counts[i] != len(groups[i]):
            return False
    return True

def find_arrangements(springs, counts, i):
    if "?" not in springs:
        return is_valid(springs, counts)
    if springs[i] != "?":
        return find_arrangements(springs, counts, i+1)
    return find_arrangements(springs[:i]+"."+springs[i+1:], counts, i+1) + find_arrangements(springs[:i]+"#"+springs[i+1:], counts, i+1)
    


if __name__ == "__main__":
    inp = [row.split() for row in  open("input.txt").read().strip().split("\n")]
    rows = []
    for springs, counts in inp:
        rows.append((springs, [int(i) for i in counts.split(",")]))
    res = 0
    for springs, counts in rows:
        res += find_arrangements(springs, counts, 0)
    print(res)
