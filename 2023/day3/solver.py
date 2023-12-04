def check_part_neightbours(schematic, i, j):
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        n = (i+d[0], j+d[1])
        if n[0] >= 0 and n[1] >= 0 and n[0] < len(schematic) and n[1] < len(schematic[0]):
            if schematic[n[0]][n[1]] not in ".0123456789":
                return True
    return False

def parse_numbers(schematic):
    numbers = set()
    number_start_idx = None
    is_part_number = False
    for i in range(len(schematic)):
        row = schematic[i]
        for j in range(len(row)):
            current = row[j]
            if current not in "01234567890":
                if number_start_idx is not None:
                    numbers.add((i, number_start_idx, j-number_start_idx, int(schematic[i][number_start_idx:j]), is_part_number))
                number_start_idx = None
                is_part_number = False
            else:
                if number_start_idx is None:
                    number_start_idx = j
                if not is_part_number:
                    is_part_number = check_part_neightbours(schematic, i, j)
        if number_start_idx is not None:
            j = len(row)
            numbers.add((i, number_start_idx, j-number_start_idx, int(schematic[i][number_start_idx:j]), is_part_number))
        number_start_idx = None
        is_part_number = False
    return numbers

if __name__ == "__main__":
    schematic = open("input.txt").read().strip().split("\n")
    numbers = parse_numbers(schematic)
    print(sum(n[3] for n in numbers if n[4]))

