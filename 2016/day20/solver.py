if __name__ == "__main__":
    bloced_ranges = open("input.txt").read().strip().split("\n")
    blocked_sorted = sorted(tuple(int(i) for i in r.split("-")) for r in bloced_ranges)
    for i in range(len(blocked_sorted)):
        if blocked_sorted[i+1][0] > blocked_sorted[i][1] + 1:
            print(blocked_sorted[i][1] + 1)
            break

