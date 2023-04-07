from collections import defaultdict

if __name__ == "__main__":
    orbits = open("input.txt").read().strip().split("\n")
    orbit_dict = defaultdict(list)
    orbited_dict = defaultdict(list)
    for orbit in orbits:
        is_orbited, orbiter = orbit.split(")")
        old_orbits = orbit_dict[orbiter]
        is_orbited_orbits = orbit_dict[is_orbited]

        orbit_dict[orbiter] = list(set([is_orbited] + is_orbited_orbits))
        is_orbited_by_orbits = orbited_dict[is_orbited]
        orbited_dict[is_orbited] = list(set([orbiter] + is_orbited_by_orbits))
        update_queue = set(orbited_dict[orbiter])
        visited = set()
        while update_queue:
            current_child_orbit = update_queue.pop()
            visited.add(current_child_orbit)
            child_obiters = orbited_dict[current_child_orbit]
            child_orbited_orbits = orbit_dict[current_child_orbit]
            orbit_dict[current_child_orbit] = list(set(orbit_dict[orbiter] + child_orbited_orbits))
            for new_orbit in child_obiters:
                if new_orbit not in visited:
                    update_queue.add(new_orbit)
    print(sum(len(orbits) for orbits in orbit_dict.values()))

