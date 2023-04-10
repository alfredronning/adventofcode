def find_longest(route_dict, current, not_visited, dist):
    if not len(not_visited):
        return dist
    longest = 0
    for city in not_visited:
        if city not in route_dict[current]:
            continue
        current_dist = find_longest(route_dict, city, [c for c in not_visited if c != city], dist+route_dict[current][city])
        longest = max(longest, current_dist)
    return longest

if __name__ == "__main__":
    routes = open("input.txt").read().strip().split("\n")
    route_dict = dict()
    for route in routes:
        cities, distance = route.split(" = ")
        f, t = cities.split(" to ")
        if f in route_dict:
            route_dict[f][t] = int(distance)
        else:
            route_dict[f] = {t: int(distance)}
        if t in route_dict:
            route_dict[t][f] = int(distance)
        else:
            route_dict[t] = {f: int(distance)}
    not_visited = list(route_dict.keys())
    longest = 0
    for city in not_visited:
        current_dist = find_longest(route_dict, city, [c for c in not_visited if c != city], 0)
        longest = max(longest, current_dist)
    print(longest)

