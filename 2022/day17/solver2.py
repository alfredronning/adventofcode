ROCKS = [
    [
        0b0011110
    ], [
        0b0001000,
        0b0011100,
        0b0001000
    ], [
        0b0000100,
        0b0000100,
        0b0011100
    ], [
        0b0010000,
        0b0010000,
        0b0010000,
        0b0010000
    ], [
        0b0011000,
        0b0011000
    ]
]

DIRECTIONS = open("input.txt").read().strip()


def push_rock(room, rock, rock_bottom, direction):
    if direction == "<":
        for i, rock_row in enumerate(rock[::-1]):
            if rock_row & 1 << 6:
                return
            if len(room) and len(room) > rock_bottom + i and rock_row << 1 & room[rock_bottom + i]:
                return
        for i, rock_row in enumerate(rock):
            rock[i] = rock_row << 1
    else:
        for i, rock_row in enumerate(rock[::-1]):
            if rock_row & 1:
                return
            if len(room) and len(room) > rock_bottom + i and rock_row >> 1 & room[rock_bottom + i]:
                return
        for i, rock_row in enumerate(rock):
            rock[i] = rock_row >> 1


def crashes_next(room, rock, rock_bottom):
    for i, rock_row in enumerate(rock[::-1]):
        if len(room) < rock_bottom + i:
            return False
        if rock_row & room[rock_bottom - 1 + i]:
            return True
    return False


def merge_rock(room, rock, rock_bottom):
    for i, rock_row in enumerate(rock[::-1]):
        if len(room) <= rock_bottom + i:
            room.append(rock_row)
        else:
            room[rock_bottom + i] |= rock_row


def simulate_rock(room, rock, time):
    rock_bottom = len(room)
    for _ in range(4):
        push_rock(room, rock, rock_bottom, DIRECTIONS[time % len(DIRECTIONS)])
        time += 1
    while True:
        if not rock_bottom or crashes_next(room, rock, rock_bottom):
            break
        rock_bottom -= 1
        push_rock(room, rock, rock_bottom, DIRECTIONS[time % len(DIRECTIONS)])
        time += 1
    merge_rock(room, rock, rock_bottom)
    return time


if __name__ == "__main__":
    time = 0
    room = []
    rocks = 2022
    hashes = {}
    rock = 0
    added_len = 0
    end_rock = 1_000_000_000_000
    while rock < end_rock:
        rocktype = ROCKS[rock % 5][:]
        time = simulate_rock(room, rocktype, time)
        h = hash((time % len(DIRECTIONS), str(room[-5:])))
        if h in hashes:
            prev_len, prev_rocks = hashes[h]
            d_rocks = rock - prev_rocks
            d_len = len(room) - prev_len
            loops = (end_rock - rock) // d_rocks
            rock += d_rocks * loops
            added_len += d_len * loops
        else:
            hashes[h] = (len(room), rock)
        rock += 1

    print(len(room) + added_len)
