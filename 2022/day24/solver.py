def sim_blizzards(board):
    new_board = [[[] for _ in range(len(board[0]))] for _ in range(len(board))]
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            for blizzard in tile:
                if blizzard == "<":
                    new_board[i][(j - 1) % len(board[0])].append(blizzard)
                if blizzard == ">":
                    new_board[i][(j + 1) % len(board[0])].append(blizzard)
                if blizzard == "^":
                    new_board[(i - 1) % len(board)][j].append(blizzard)
                if blizzard == "v":
                    new_board[(i + 1) % len(board)][j].append(blizzard)
    return new_board


def hueristic(pos, endpos, steps):
    return endpos[0] - pos[0] + endpos[1] - pos[1] + steps * steps


def insert_by_hueristic(queue, item):
    for i in range(len(queue)):
        if item[-1] <= queue[i][-1]:
            queue.insert(i, item)
            return
    queue.append(item)


def find_shortest(board, endpos, startpos):
    shortest = float("inf")
    board_by_steps = {}
    queue = [(startpos, board, 0, hueristic(startpos, endpos, 0))]
    checked = {(startpos, 0)}
    while queue:
        current_pos, current_board, current_steps, _ = queue.pop(0)
        if current_steps in board_by_steps:
            current_board = board_by_steps[current_steps]
        else:
            current_board = sim_blizzards(current_board)
            board_by_steps[current_steps] = current_board
        if current_pos == endpos:
            shortest = min(shortest, current_steps)
        if current_steps >= shortest:
            continue
        current_steps += 1
        for move in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = current_pos[0] + move[0], current_pos[1] + move[1]
            h = hueristic(next_pos, endpos, current_steps)
            if next_pos == endpos or next_pos == startpos:
                if (next_pos, current_steps + 1) not in checked:
                    insert_by_hueristic(queue, (next_pos, current_board, current_steps, h))
                    checked.add((next_pos, current_steps + 1))
            elif next_pos[0] >= 0 and next_pos[1] >= 0 and next_pos[0] < len(board) and next_pos[1] < len(board[0]):
                if not len(current_board[next_pos[0]][next_pos[1]]):
                    if (next_pos, current_steps) not in checked:
                        insert_by_hueristic(queue, (next_pos, current_board, current_steps, h))
                        checked.add((next_pos, current_steps))
    return shortest


if __name__ == "__main__":
    board = [[[i] if i in "<>^v" else [] for i in row[1:-1]] for row in
             open("input.txt").read().strip().split("\n")[1:-1]]
    startpos = (-1, 0)
    endpos = (len(board), len(board[0]) - 1)
    print(find_shortest(board, endpos, startpos))
