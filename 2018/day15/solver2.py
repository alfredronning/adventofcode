from collections import defaultdict

class Unit:
    def __init__(self, type, x, y, dammage):
        self.type = type
        self.pos = (x, y)
        self.dammage = dammage
        self.hp = 200


def sorted_add(open_set, scores, item):
    for i, cmp_item in enumerate(open_set):
        if scores[item] < scores[cmp_item]:
            open_set.insert(i, item)
            return
    open_set.append(item)


def a_star(board, units_pos, start, end):
    open_set = [start]
    came_from = {start: None}
    length = defaultdict(lambda: float("inf"))
    length[start] = 0
    h = lambda s, e: ((e[0]-s[0])**2+(e[1]-s[1])**2)**0.5
    scores = defaultdict(lambda: float("inf"))
    scores[start] = h(start, end)
    while open_set:
        current = open_set[0]
        if current == end:
            i = 0
            while came_from[current] is not None:
                i += 1
                current = came_from[current]
            return i
        open_set = open_set[1:]
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbour = (current[0]+d[0], current[1]+d[1])
            if board[neighbour[0]][neighbour[1]] and (neighbour == end or neighbour not in units_pos):
                if length[current]+1 < length[neighbour]:
                    came_from[neighbour] = current
                    length[neighbour] = length[current]+1
                    scores[neighbour] = length[current]+1+h(neighbour, end)
                    if neighbour not in open_set:
                        sorted_add(open_set, scores, neighbour)
    return None


def find_attack_target(unit, units):
    attack_candidates = []
    for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_tile = (unit.pos[0]+d[0], unit.pos[1]+d[1])
        for other_unit in units:
            if unit == other_unit or unit.type == other_unit.type:
                continue
            if new_tile == other_unit.pos:
                attack_candidates.append(other_unit)
    if not attack_candidates:
        return
    return sorted(attack_candidates, key=lambda u: (u.hp, u.pos))[0]


def find_move_tile(unit, units, board, dead):
    move_candidates = []
    move_dists = []
    unit_pos = set(u.pos for u in units if u not in dead)
    for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_tile = (unit.pos[0]+d[0], unit.pos[1]+d[1])
        if not board[new_tile[0]][new_tile[1]]:
            continue
        min_dist = float("inf")
        for other_unit in [u for u in units if u not in dead]:
            if new_tile == other_unit.pos and unit.type != other_unit.type:
                return
            if unit.type != other_unit.type:
                dist = a_star(board, unit_pos, new_tile, other_unit.pos)
                if dist:
                    min_dist = min(min_dist, dist)
        if new_tile not in unit_pos and min_dist != float("inf"):
            move_candidates.append(new_tile)
            move_dists.append(min_dist)
    if not move_candidates:
        return
    min_dist=min(move_dists)
    move_candidates = [move_candidates[i] for i in range(len(move_candidates)) if move_dists[i] == min_dist]
    return sorted(move_candidates)[0]


def simulate(units, board):
    units.sort(key=lambda u: u.pos)
    dead = set()
    for unit in units:
        if unit in dead:
            continue

        move_tile = find_move_tile(unit, units, board, dead)
        if move_tile:
            unit.pos = move_tile

        attack_target = find_attack_target(unit, [u for u in units if u not in dead])
        if attack_target:
            attack_target.hp -= unit.dammage
            if attack_target.hp <= 0:
                if attack_target.type == "E":
                    return False
                dead.add(attack_target)
                if unit != units[-1]:
                    alive_elfs = [u for u in units if u.hp > 0 and u.type == "E"]
                    alive_goblins = [u for u in units if u.hp > 0 and u.type == "G"]
                    if not alive_elfs or not alive_goblins:
                        return False
    for unit in dead:
        units.remove(unit)

    return True


def print_board(board, units, round):
    print("---------------------------------------------------------")
    print(round)
    unit_pos = set(u.pos for u in units)
    for i, line in enumerate(board):
        row = ""
        postfix_hp = []
        for j, tile in enumerate(line):
            if (i, j) not in unit_pos:
                row += "." if tile else "#"
            else:
                unit = [u for u in units if u.pos == (i, j)][0]
                postfix_hp.append(str(unit.hp))
                row += unit.type
        print(row + " " + ", ".join(postfix_hp))
    print("---------------------------------------------------------")

def elf_win(board, units):
    pass
    round = 0
    while True:
        #print_board(board, units, round)
        if not simulate(units, board):
            break
        alive_goblins = [u for u in units if u.hp > 0 and u.type == "G"]
        round += 1
        if not alive_goblins:
            break

    alive_goblins = [u for u in units if u.hp > 0 and u.type == "G"]
    if not alive_goblins:
        print("Elfs win after round: " + str(round))
        hp = sum(u.hp for u in units if u.type == "E")
        print("wins with remainding hitpoints " + str(hp))
        print("Outcome: "+ str(round*hp))
        return round*hp
    else:
        print("elfs died :/")


if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    new_board = []
    for i, line in enumerate(board):
        row = []
        for j, tile in enumerate(line):
            if tile in "EG":
                row.append(True)
            elif tile == "#":
                row.append(False)
            else:
                row.append(True)
        new_board.append(row)
    elf_attack = 29
    while True:
        units = []
        print(elf_attack)
        for i, line in enumerate(board):
            for j, tile in enumerate(line):
                if tile == "E":
                    units.append(Unit(tile, i, j, elf_attack))
                elif tile == "G":
                    units.append(Unit(tile, i, j, 3))
        e_win = elf_win(new_board, units)
        if e_win:
            break
        elf_attack += 1

