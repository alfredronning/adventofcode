def is_accepted(workflows, current_workflow, part):
    rules = workflows[current_workflow]
    i = 0
    while i < len(rules):
        rule = rules[i]
        if rule == "A":
            return True
        if rule == "R":
            return False
        if rule in workflows:
            return is_accepted(workflows, rule, part)
        if ">" in rule:
            category, value = rule.split(">")
            if part[category] > int(value):
                i += 1
            else:
                i += 2
        else:
            category, value = rule.split("<")
            if part[category] < int(value):
                i += 1
            else:
                i += 2


if __name__ == "__main__":
    workflows, parts = open("input.txt").read().strip().split("\n\n")
    parts = [dict((e.split("=")[0], int(e.split("=")[1])) for e in p[1:-1].split(",")) for p in parts.split("\n")]
    workflows = dict((w.split("{")[0], w[:-1].split("{")[1].replace(":", ",").split(",")) for w in workflows.split("\n"))
    res = 0
    for part in parts:
        if is_accepted(workflows, "in", part):
            res += sum(part.values())
    print(res)

