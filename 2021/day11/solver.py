def simulate_flashes(octopuses):
    flashed = set()
    for row in range(10):
        for col in range(10):
            if octopuses[row][col] == 9:
                flashed.add((row, col))
                octopuses[row][col] = 0
            else:
                octopuses[row][col] += 1
    last_flashed = 0
    checked = set()
    while last_flashed != len(flashed):
        last_flashed = len(flashed)
        for octo in list(flashed):
            if octo in checked:
                continue
            checked.add(octo)
            for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                neighbour = octo[0] + direction[0], octo[1] + direction[1]
                if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<10 and neighbour[1]<10:
                    if neighbour not in flashed:
                        if octopuses[neighbour[0]][neighbour[1]] == 9:
                            flashed.add(neighbour)
                            octopuses[neighbour[0]][neighbour[1]] = 0
                        else:
                            octopuses[neighbour[0]][neighbour[1]] += 1
    return len(flashed)

if __name__ == "__main__":
    octopuses = [[int(octo) for octo in row] for row in open("input.txt").read().strip().split("\n")]
    flashes = 0
    for _ in range(100):
        flashes += simulate_flashes(octopuses)
    print(flashes)

