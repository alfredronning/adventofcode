if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    infected = set()
    bursts = 10000
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
        else:
            current_dir = (current_dir-1)%len(directions)
            infected.add(carrier_pos)
            infected_bursts += 1
        carrier_pos = (carrier_pos[0]+directions[current_dir][0], carrier_pos[1]+directions[current_dir][1])
    
    print(infected_bursts)

