import re

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

if __name__ == "__main__":
    flips = open("input.txt").read().strip().split("\n")
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
    print(len(flipped))

