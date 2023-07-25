if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    infected = set()
    weakened = set()
    flagged = set()
    bursts = 10000000
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "#":
                infected.add((i, j))

    carrier_pos = (len(board)//2, len(board[0])//2)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0
    infected_bursts = 0
    for _ in range(bursts):
        if carrier_pos in infected:
            current_dir = (current_dir+1)%len(directions)
            infected.remove(carrier_pos)
            flagged.add(carrier_pos)
        elif carrier_pos in weakened:
            weakened.remove(carrier_pos)
            infected.add(carrier_pos)
            infected_bursts += 1
        elif carrier_pos in flagged:
            current_dir = (current_dir+2)%len(directions)
            flagged.remove(carrier_pos)
        else:
            current_dir = (current_dir-1)%len(directions)
            weakened.add(carrier_pos)
        carrier_pos = (carrier_pos[0]+directions[current_dir][0], carrier_pos[1]+directions[current_dir][1])
    
    print(infected_bursts)

