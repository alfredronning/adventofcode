def convert_ranges(map, seed_range):
    queue = [seed_range]
    res = []
    while len(queue):
        current_s, current_r = queue.pop()
        changed = False
        for dest, source, r in map:
            if current_s + current_r <= source or current_s >= source + r:
                continue
            if current_s >= source and current_s + current_r <= source + r:
                res.append((current_s - source + dest, current_r))
                changed = True
                break
            if current_s < source and current_s + current_r > source + r:
                res.append((source, r))
                queue.append((current_s, source-current_s))
                queue.append((source+r, current_s+current_r-source-r))
                changed = True
                break
            if current_s < source and current_s + current_r < source + r:
                res.append((source, current_r+current_s-source))
                queue.append((current_s, source-current_s))
                changed = True
                break
            if current_s > source and current_s + current_r > source + r:
                res.append((current_s, source+r-current_s))
                queue.append((source+r, current_s+current_r-source-r))
                changed = True
                break
        if not changed:
            res.append((current_s, current_r))
    return res

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n\n")
    seeds = [int(i) for i in inp[0].split(": ")[1].split()]
    seeds_ranges = [(seeds[i*2], seeds[i*2+1]) for i in range(len(seeds)//2)]
    maps = [[], [], [], [], [], [], []]
    for i in range(len(maps)):
        rows = inp[i+1].split("\n")[1:]
        for row in rows:
            maps[i].append(tuple([int(k) for k in row.split()]))

    for m in range(len(maps)):
        new_seed_ranges = []
        for r in seeds_ranges:
            new_seed_ranges += convert_ranges(maps[m], r)
        seeds_ranges = new_seed_ranges
    print(min(r[0] for r in seeds_ranges))

