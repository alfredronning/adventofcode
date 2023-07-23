def reallocate(banks):
    maxidx = banks.index(max(banks))
    realloc_val = banks[maxidx]
    banks[maxidx] = 0
    for i in range(len(banks)):
        banks[i] += realloc_val//len(banks)
    for i in range(realloc_val - realloc_val//len(banks)*len(banks)):
        banks[(maxidx+i+1)%len(banks)] += 1

if __name__ == "__main__":
    banks = [int(i) for i in open("input.txt").read().strip().split()]
    seen = set()
    steps = 0

    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        steps += 1

        reallocate(banks)
    print(steps)

