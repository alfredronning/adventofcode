def real_room(room):
    splits = room.split("-")
    letters = "".join(splits[:-1])
    checksum = splits[-1].split("[")[1][:-1]
    counts = list(set((-letters.count(c), c) for c in letters))
    counts.sort()
    return "".join(tup[1] for tup in counts[:5]) == checksum

def decrypt_room(room):
    splits = room.split("-")
    letters = "".join(splits[:-1])
    checksum = splits[-1].split("[")[1][:-1]
    sector_id = int(splits[-1].split("[")[0])

    res = ""
    for c in "-".join(splits[:-1]):
        if c == "-":
            res += "-"
        else:
            res += chr((ord(c)-ord("a")+sector_id)%26+ord("a"))
    return res, sector_id

if __name__ == "__main__":
    rooms = open("input.txt").read().strip().split("\n")
    for room in rooms:
        if real_room(room):
            room_name, sector_id = decrypt_room(room)
            print(room_name, sector_id)

