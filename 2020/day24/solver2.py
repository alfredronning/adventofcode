def get_moves(flip):
    moves = []
    i = 0
    while i < len(flip):
        if flip[i] in ["w", "e"]:
            moves.append(flip[i])
            i += 1
        else:
            moves.append(flip[i:i+2])
            i += 2
    return moves

def flip_inital(flips):
    flipped = set()
    for flip in flips:
        reference_tile = [0, 0]
        moves = get_moves(flip)
        for move in moves:
            if move == "e":
                reference_tile[0] += 2
            elif move == "w":
                reference_tile[0] -= 2
            elif move == "se":
                reference_tile[0] += 1
                reference_tile[1] += 1
            elif move == "sw":
                reference_tile[0] -= 1
                reference_tile[1] += 1
            elif move == "ne":
                reference_tile[0] += 1
                reference_tile[1] -= 1
            elif move == "nw":
                reference_tile[0] -= 1
                reference_tile[1] -= 1
        destination_tile = tuple(reference_tile)
        if destination_tile in flipped:
            flipped.remove(destination_tile)
        else:
            flipped.add(destination_tile)
    return flipped

def simulate_day(flipped):
    new_flipped = set()
    unflipped_count = dict()
    for tile in flipped:
        flipped_neighbours = 0
        for d in [(2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            neighbour = (tile[0]+d[0], tile[1]+d[1])
            if neighbour in flipped:
                flipped_neighbours += 1
            else:
                if neighbour in unflipped_count:
                    unflipped_count[neighbour] += 1
                else:
                    unflipped_count[neighbour] = 1
        if flipped_neighbours in [1, 2]:
            new_flipped.add(tile)
    for unflipped in unflipped_count:
        if unflipped_count[unflipped] == 2:
            new_flipped.add(unflipped)
    return new_flipped

if __name__ == "__main__":
    flips = open("input.txt").read().strip().split("\n")
    flipped = flip_inital(flips)
    for _ in range(100):
        flipped = simulate_day(flipped)
    print(len(flipped))

