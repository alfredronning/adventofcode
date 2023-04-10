def find_max_happiness(happiness_dict, current_person, not_visited, happiness):
    if not len(not_visited):
        return happiness + happiness_dict[current_person]["Alice"] + happiness_dict["Alice"][current_person]
    res = 0
    for next_person in not_visited:
        next_happiness = happiness + happiness_dict[current_person][next_person] + happiness_dict[next_person][current_person]
        next_not_visited = [i for i in not_visited if i != next_person]
        current_happiness = find_max_happiness(happiness_dict, next_person, next_not_visited, next_happiness)
        res = max(res, current_happiness)
    return res

if __name__ == "__main__":
    happiness = open("input.txt").read().strip().split("\n")
    happiness_dict = {}
    for row in happiness:
        s = row.split()
        p1, p2, points, sign = s[0], s[-1][:-1], s[3], s[2]
        if p1 in happiness_dict:
            happiness_dict[p1][p2] = int(points)*(1 if sign == "gain" else -1)
        else:
            happiness_dict[p1] = {p2: int(points)*(1 if sign == "gain" else -1)}

    start_person = "Alice"
    not_visited = [p for p in happiness_dict if p != start_person]
    max_happiness = find_max_happiness(happiness_dict, start_person, not_visited, 0)
    print(max_happiness)

