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
    energized.remove(start[0])
    return len(energized)

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    start = ((0, -1), (0, 1))
    energized = simulate(inp, start)
    print(energized)
