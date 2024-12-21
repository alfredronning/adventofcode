towels, patterns = open("input.txt").read().strip().split("\n\n")
towels = towels.split(", ")
patterns = patterns.split()

cache = dict()

def can_make(pattern, towels, cache):
    if len(pattern) == 0:
        return 1
    if pattern in cache:
        return cache[pattern]
    total_permutations = 0
    for towel in towels:
        if pattern[:len(towel)] == towel:
            total_permutations += can_make(pattern[len(towel):], towels, cache)
    cache[pattern] = total_permutations
    return total_permutations

res = 0
for pattern in patterns:
    res += can_make(pattern, towels, cache)
print(res)


