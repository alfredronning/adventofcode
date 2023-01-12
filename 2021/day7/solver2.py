if __name__ == "__main__":
    crabs = [int(c) for c in open("input.txt").read().strip().split(",")]
    avg = int(sum(crabs)/len(crabs))
    res = float("inf")
    for i in range(avg, max(crabs)):
        current = sum(sum(range(abs(crab-i)+1)) for crab in crabs)
        if current > res:
            break
        res = current
    for i in range(avg-1, -1, -1):
        current = sum(sum(range(abs(crab-i)+1)) for crab in crabs)
        if current > res:
            break
        res = current
    print(res)
    
