def matches(inp, rule_dict, current_rule, i):
    if not i < len(inp):
        return False, i
    # terminal node
    if current_rule not in rule_dict:
        if inp[i] == current_rule:
            return True, i+1
        return False, i
    for rule_path in rule_dict[current_rule]:
        allmatch = True
        next_i = i
        for next_rule in rule_path:
            match, next_i = matches(inp, rule_dict, next_rule, next_i)
            if not match:
                allmatch = False
                break
        if allmatch:
            return True, next_i
    return False, i

if __name__ == "__main__":
    rules, messages = open("testinput.txt").read().strip().split("\n\n")
    rule_dict = dict()
    for rule in rules.split("\n"):
        ruleid, applied_rules = rule.split(": ")
        rule_paths = []
        for rule_path in applied_rules.replace("\"", "").split(" | "):
            rule_paths.append(rule_path.split())
        rule_dict[ruleid] = rule_paths

    res = 0
    for message in messages.split("\n"):
        match, i = matches(message, rule_dict, "0", 0)
        if match and i == len(message):
            res += 1
    print(res)

