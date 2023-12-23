def simulate_fall(brick_map, occupied):
    changed = True
    while changed:
        changed = False
        for brick_idx in brick_map:
            if any((b[0], b[1], b[2]-1) in occupied and (b[0], b[1], b[2]-1) not in brick_map[brick_idx] for b in brick_map[brick_idx]):
                continue
            if any(b[2] == 1 for b in brick_map[brick_idx]):
                continue
            new_bricks = []
            changed = True
            for brick in sorted(brick_map[brick_idx], key=lambda x: x[2]):
                new_brick = (brick[0], brick[1], brick[2]-1)
                new_bricks.append(new_brick)
                occupied.remove(brick)
                occupied.add(new_brick)
            brick_map[brick_idx] = new_bricks

def bricks_fall(brick_map, occupied):
    for brick_idx in brick_map:
        if any((b[0], b[1], b[2]-1) in occupied and (b[0], b[1], b[2]-1) not in brick_map[brick_idx] for b in brick_map[brick_idx]):
            continue
        if any(b[2] == 1 for b in brick_map[brick_idx]):
            continue
        return True
    return False


bricks = [(tuple(int(i) for i in b.split("~")[0].split(",")), tuple(int(i) for i in b.split("~")[1].split(","))) for b in open("input.txt").read().strip().split("\n")]

brick_map = dict()
occupied = set()

for i, brick in enumerate(bricks):
    first, last = brick
    brick_map[i] = set()
    if first[0] != last[0]:
        for x in range(first[0], last[0]+1):
            brick_map[i].add((x, first[1], first[2]))
            occupied.add((x, first[1], first[2]))
    elif first[1] != last[1]:
        for y in range(first[1], last[1]+1):
            brick_map[i].add((first[0], y, first[2]))
            occupied.add((first[0], y, first[2]))
    else:
        for z in range(first[2], last[2]+1):
            brick_map[i].add((first[0], first[1], z))
            occupied.add((first[0], first[1], z))

simulate_fall(brick_map, occupied)
res = 0
for brick_idx in brick_map:
    occupied_cp = occupied.copy()
    for b in brick_map[brick_idx]:
        occupied_cp.remove(b)
    if not bricks_fall(brick_map, occupied_cp):
        res += 1
print(res)
