def simulate(inp, start):
    visited = set()
    energized = set()
    beams = [start]
    while beams:
        next_beams = []
        for pos, dir in beams:
            energized.add(pos)
            if (pos, dir) in visited:
                continue
            newpos = (pos[0]+dir[0], pos[1]+dir[1])
            if newpos[0] < 0 or newpos[0] >= len(inp) or newpos[1] < 0 or newpos[1] >= len(inp[0]):
                continue
            mirror = inp[newpos[0]][newpos[1]]
            if mirror == ".":
                if (newpos, dir) not in visited:
                    next_beams.append((newpos, dir))
            elif mirror in "|-":
                if dir[0] and mirror == "|" or dir[1] and mirror == "-":
                    next_beams.append((newpos, dir))
                elif dir[0]:
                    next_beams.append((newpos, (0, 1)))
                    next_beams.append((newpos, (0, -1)))
                else:
                    next_beams.append((newpos, (1, 0)))
                    next_beams.append((newpos, (-1, 0)))
            elif mirror == "\\":
                next_beams.append((newpos, (dir[1], dir[0])))
            else:
                next_beams.append((newpos, (-dir[1], -dir[0])))
        visited.update(beams)
        beams = next_beams
    energized.remove((start[0]))
    return len(energized)

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    max_res = 0
    for i in range(len(inp)):
        max_res = max(max_res, simulate(inp, ((i, -1), (0, 1))))
        max_res = max(max_res, simulate(inp, ((i, len(inp[i])), (0, -1))))
    for i in range(len(inp[0])):
        max_res = max(max_res, simulate(inp, ((-1, i), (1, 0))))
        max_res = max(max_res, simulate(inp, ((len(inp[i]), i), (-1, 0))))
    print(max_res)
