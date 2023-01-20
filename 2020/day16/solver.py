import re

if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = open("input.txt").read().strip().split("\n\n")
    ranges = []
    for rule in rules.split("\n"):
        numbers = re.findall(r".*: (\d*)-(\d*) or (\d*)-(\d*)", rule)[0]
        for i in range(len(numbers)//2):
            ranges.append((int(numbers[i*2]), int(numbers[i*2+1])))
    res = 0
    for ticket in nearby_tickets.split("\n")[1:]:
        for field in [int(i) for i in ticket.split(",")]:
            if not any(field >= range[0] and field <= range[1] for range in ranges):
                res += field
    print(res)

