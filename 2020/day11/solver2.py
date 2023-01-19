def printseats(seatmap, h, w):
    for i in range(h):
        row = ""
        for j in range(w):
            if seatmap[(i, j)] == -1:
                row += "."
            if seatmap[(i, j)] == 0:
                row += "L"
            if seatmap[(i, j)] == 1:
                row += "#"
        print(row)
    print()

def count_empty(seat_map, seat, h, w):
    neighbours_count = 0
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        n = (seat[0] + d[0], seat[1] + d[1])
        while n[0] >= 0 and n[1] >= 0 and n[0] < h and n[1] < w:
            if seat_map[n] == 1:
                neighbours_count += 1
            if seat_map[n] >= 0:
                break
            n = (n[0] + d[0], n[1] + d[1])
    return neighbours_count

if __name__ == "__main__":
    room = open("input.txt").read().strip().split("\n")
    h, w = len(room), len(room[0])
    seat_map = dict()
    for i, row in enumerate(room):
        for j, seat in enumerate(row):
            if seat == "L":
                seat_map[(i, j)] = 0
            else:
                seat_map[(i, j)] = -1
    changed = True
    while changed:
        changed = False
        new_seats = dict()
        for seat in seat_map:
            if seat_map[seat] == -1:
                new_seats[seat] = seat_map[seat]
                continue
            neighbours_count = count_empty(seat_map, seat, h, w)
            if seat_map[seat] == 0 and neighbours_count == 0:
                new_seats[seat] = 1
                changed = True
            elif seat_map[seat] == 1 and neighbours_count >= 5:
                new_seats[seat] = 0
                changed = True
            else:
                new_seats[seat] = seat_map[seat]
        seat_map = new_seats

print(sum(seat == 1 for seat in seat_map.values()))
