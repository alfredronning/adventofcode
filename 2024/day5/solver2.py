from collections import defaultdict

rules, updates = open("input.txt").read().strip().split("\n\n")

afters = defaultdict(set)
for rule in rules.split("\n"):
    x, y = rule.split("|")
    afters[x].add(y)

res = 0

def right(afters, update):
    for i in range(len(update)):
        back = update[-1-i]
        rest = update[:-1-i]
        if any(i in afters[back] for i in rest):
            return False
    return True

def correct(afters, update):
    for i in range(len(update)):
        back = update[-1-i]
        rest = update[:-1-i]
        for j in range(len(rest)):
            if rest[j] in afters[back]:
                update[-1-i] = rest[j]
                update[j] = back
                return correct(afters, update)
    return update

    
updates = [u.split(",") for u in updates.split("\n")]

invalid_updates = [u for u in updates if not right(afters, u)]
corrected_updates = [correct(afters, u) for u in invalid_updates]
mid_corrected = [int(u[len(u)//2]) for u in corrected_updates]

print(sum(mid_corrected))

