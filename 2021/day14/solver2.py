from collections import Counter

def apply_rules(counter, rules):
    new_counter = Counter()
    for pair in counter:
        if pair in rules:
            first = pair[0]+rules[pair]
            second = rules[pair] + pair[1]
            new_counter[first] += counter[pair]
            new_counter[second] += counter[pair]
    return new_counter

if __name__ == "__main__":
    template, rules = open("input.txt").read().strip().split("\n\n")
    rules = dict(rule.split(" -> ") for rule in rules.split("\n"))
    counter = Counter()
    for i in range(len(template)-1):
        counter[template[i:i+2]] += 1
    for _ in range(40):
        counter = apply_rules(counter, rules)
    char_counter = Counter()
    for count in counter:
        char_counter[count[0]] += counter[count]
    char_counter[template[-1]] += 1
    print(max(char_counter.values())-min(char_counter.values()))

