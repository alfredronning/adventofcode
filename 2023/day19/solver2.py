def count_accepted(workflows, current_workflow, bounds, i):
    rules = workflows[current_workflow]
    rule = rules[i]
    if any(b[1] < b[0] for b in bounds.values()):
        return 0
    if rule == "R":
        return 0
    if rule == "A":
        res = 1
        for b in bounds.values():
            res *= b[1]-b[0]+1
        return res
    if rule in workflows:
        return count_accepted(workflows, rule, bounds, 0)
    category, value = rule.replace("<", ">").split(">")
    value = int(value)
    bounds_over = bounds.copy()
    bounds_under = bounds.copy()
    bounds_over[category] = (max(bounds[category][0], value+(1 if ">" in rule else 0)), bounds[category][1])
    bounds_under[category] = (bounds[category][0], min(bounds[category][1], value+(0 if ">" in rule else -1)))
    res = count_accepted(workflows, current_workflow, bounds_over if ">" in rule else bounds_under, i+1)
    res += count_accepted(workflows, current_workflow, bounds_under if ">" in rule else bounds_over, i+2)
    return res


if __name__ == "__main__":
    workflows = open("input.txt").read().strip().split("\n\n")[0]
    workflows = dict((w.split("{")[0], w[:-1].split("{")[1].replace(":", ",").split(",")) for w in workflows.split("\n"))
    res = 0
    bounds = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    print(count_accepted(workflows, "in", bounds, 0))

