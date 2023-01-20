import re

def is_valid_ticket(ticket, ranges):
    for field in [int(i) for i in ticket.split(",")]:
        if not any((field >= r[0][0] and field <= r[0][1]) or (field >= r[1][0] and field <= r[1][1]) for r in ranges):
            return False
    return True

if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = open("input.txt").read().strip().split("\n\n")
    rule_ranges = []

    departure_ids = set()
    # collect all the rules
    for rule_id, rule in enumerate(rules.split("\n")):
        numbers = re.findall(r".*: (\d*)-(\d*) or (\d*)-(\d*)", rule)[0]
        dep_ranges = []
        for i in range(len(numbers)//2):
            dep_ranges.append((int(numbers[i*2]), int(numbers[i*2+1])))
        rule_ranges.append(dep_ranges)
        if "departure" in rule:
            departure_ids.add(rule_id)

    # remove invalid nearby tickets
    nearby_tickets = [[int(i) for i in ticket.split(",")] for ticket in nearby_tickets.split("\n")[1:] if is_valid_ticket(ticket, rule_ranges)]
    my_ticket = [int(i) for i in my_ticket.split("\n")[1].split(",")]
    possible_rule_fields = dict()

    # find possible fields for each rule
    for rule_id in range(len(rule_ranges)):
        range1, range2 = rule_ranges[rule_id]
        possible_fields = []
        for field_id in range(len(my_ticket)):
            if all((ticket[field_id] >= range1[0] and ticket[field_id] <= range1[1])
                       or (ticket[field_id] >= range2[0] and ticket[field_id] <= range2[1]) for ticket in nearby_tickets):
                possible_fields.append(field_id)
        possible_rule_fields[rule_id] = possible_fields

    # remove only choices from other sets utill all are left with one choice
    one_choice = set()
    changed = True
    while changed:
        changed = False
        for rule_id in range(len(my_ticket)):
            if rule_id in one_choice:
                continue
            if len(possible_rule_fields[rule_id]) == 1:
                choice = possible_rule_fields[rule_id][0]
                one_choice.add(rule_id)
                changed = True
                for rule_id2 in range(len(my_ticket)):
                    if rule_id == rule_id2:
                        continue
                    if choice in possible_rule_fields[rule_id2]:
                        possible_rule_fields[rule_id2].remove(choice)
                break

    res = 1
    for dep_id in departure_ids:
        res *= my_ticket[possible_rule_fields[dep_id][0]]
    print(res)


