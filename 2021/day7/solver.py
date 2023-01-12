if __name__ == "__main__":
    crabs = sorted(int(c) for c in open("input.txt").read().strip().split(","))
    mid = crabs[len(crabs)//2]
    print(sum(abs(crab-mid) for crab in crabs))

