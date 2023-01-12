def apply_rules(template, rules):
    res = ""
    for i in range(len(template)):
        res += template[i]
        duo = template[i:i+2]
        if duo in rules:
            res += rules[duo]
    return res

if __name__ == "__main__":
    template, rules = open("input.txt").read().strip().split("\n\n")
    rules = dict(rule.split(" -> ") for rule in rules.split("\n"))
    for _ in range(21):
        template = apply_rules(template, rules)
    quantities = sorted(template.count(i) for i in set(template))
    print(quantities[-1]-quantities[0])

