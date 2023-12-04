def check_part_neightbours(schematic, i, j):
    res = set()
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        n = (i+d[0], j+d[1])
        if n[0] >= 0 and n[1] >= 0 and n[0] < len(schematic) and n[1] < len(schematic[0]):
            if schematic[n[0]][n[1]] == "*":
                res.add(n)
    return res

def find_gear_neighbours(schematic):
    numbers = set()
    number_start_idx = None
    gear_neightbours = set()
    for i in range(len(schematic)):
        row = schematic[i]
        for j in range(len(row)):
            current = row[j]
            if current not in "01234567890":
                if number_start_idx is not None and len(gear_neightbours):
                    numbers.add((i, number_start_idx, int(schematic[i][number_start_idx:j]), frozenset(gear_neightbours)))
                number_start_idx = None
                gear_neightbours = set()
            else:
                if number_start_idx is None:
                    number_start_idx = j
                gear_neightbours.update(check_part_neightbours(schematic, i, j))
        if number_start_idx is not None and len(gear_neightbours):
            j = len(row)
            numbers.add((i, number_start_idx, int(schematic[i][number_start_idx:j]), frozenset(gear_neightbours)))
        number_start_idx = None
        gear_neightbours = set()
    return numbers

def find_gears(numbers):
    gears = set()
    for n in numbers:
        for gear in n[3]:
            gears.add(gear)
    return gears


if __name__ == "__main__":
    schematic = open("input.txt").read().strip().split("\n")
    numbers = find_gear_neighbours(schematic)
    gears = set()
    res = 0
    for gear in find_gears(numbers):
        gearnumbers = []
        for number in numbers:
            if gear in number[3]:
                gearnumbers.append(number[2])
        if len(gearnumbers) == 2:
            res += gearnumbers[0]*gearnumbers[1]
    print(res)

