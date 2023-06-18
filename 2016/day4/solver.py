def real_room(letters, checksum):
    counts = list(set((-letters.count(c), c) for c in letters))
    counts.sort()
    return "".join(tup[1] for tup in counts[:5]) == checksum

def calc_sector_id(room):
    splits = room.split("-")
    letters = "".join(splits[:-1])
    checksum = splits[-1].split("[")[1][:-1]
    sector_id = int(splits[-1].split("[")[0])
    if real_room(letters, checksum):
        return sector_id
    return 0

if __name__ == "__main__":
    rooms = open("input.txt").read().strip().split("\n")
    res = 0
    for room in rooms:
        res += calc_sector_id(room)
    print(res)

