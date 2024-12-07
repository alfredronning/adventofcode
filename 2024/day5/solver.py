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

updates = [u.split(",") for u in updates.split("\n")]

valid_updates = [u for u in updates if right(afters, u)]
mid_valid = [int(u[len(u)//2]) for u in valid_updates]

print(sum(mid_valid))

