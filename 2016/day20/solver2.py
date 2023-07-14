if __name__ == "__main__":
    bloced_ranges = open("input.txt").read().strip().split("\n")
    blocked_sorted = sorted(tuple(int(i) for i in r.split("-")) for r in bloced_ranges)
    allowed = 0
    blocked_non_covered = []
    current_max = 0
    for r in blocked_sorted:
        if r[1] <= current_max:
            continue
        blocked_non_covered.append(r)
        current_max = r[1]
    for i in range(len(blocked_non_covered)-1):
        if blocked_non_covered[i+1][0] > blocked_non_covered[i][1] + 1:
            allowed += blocked_non_covered[i+1][0] - (blocked_non_covered[i][1] + 1)
    print(allowed)

