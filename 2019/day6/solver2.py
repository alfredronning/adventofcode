from collections import defaultdict

def dfs(current, neighbour_dict, visited, stepcount):
    if current == "SAN":
        return stepcount - 2
    visited.add(current)
    neighbours = [orbit for orbit in neighbour_dict[current] if orbit not in visited]
    for neighbour in neighbours:
        res = dfs(neighbour, neighbour_dict, visited, stepcount + 1)
        if res:
            return res
    return False

if __name__ == "__main__":
    orbits = open("input.txt").read().strip().split("\n")
    neighbour_dict = defaultdict(list)
    for orbit in orbits:
        is_orbited, orbiter = orbit.split(")")
        neighbour_dict[orbiter].append(is_orbited)
        neighbour_dict[is_orbited].append(orbiter)
    print(dfs("YOU", neighbour_dict, set(), 0))

