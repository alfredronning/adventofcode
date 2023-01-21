def matches(inp, rule_dict, current_rule, i):
    if not i < len(inp):
        return []
    # terminal node
    if current_rule not in rule_dict:
        if inp[i] == current_rule:
            return [i+1]
        return []
    all_legal_paths = []
    for rule_path in rule_dict[current_rule]:
        legal_paths_rule = [i]
        for next_rule in rule_path:
            this_path_paths = legal_paths_rule[:]
            legal_paths_rule = []
            while this_path_paths:
                i_path = this_path_paths.pop(0)
                next_i = matches(inp, rule_dict, next_rule, i_path)
                legal_paths_rule += next_i
        all_legal_paths += legal_paths_rule
    return all_legal_paths

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
        match = matches(message, rule_dict, "0", 0)
        if len(message) in match:
            res += 1
    print(res)

