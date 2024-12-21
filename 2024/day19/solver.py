towels, patterns = open("input.txt").read().strip().split("\n\n")
towels = towels.split(", ")
patterns = patterns.split()

cache = dict()

def can_make(pattern, towels, cache):
    if len(pattern) == 0:
        return True
    if pattern in cache:
        return cache[pattern]
    for towel in towels:
        if pattern[:len(towel)] == towel:
            if can_make(pattern[len(towel):], towels, cache):
                cache[pattern] = True
                return True
            else:
                cache[pattern] = False
    return False

res = 0
for pattern in patterns:
    if can_make(pattern, towels, cache):
        res += 1
print(res)


