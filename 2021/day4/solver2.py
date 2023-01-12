def has_won(numbers, board):
    for row in board:
        if all(n in numbers for n in row):
            return True
    for i in range(len(board[0])):
        if all(n in numbers for n in [board[j][i] for j in range(len(board))]):
            return True
    return False

def find_winner_score(numbers, boards):
    number_pointer = 0
    current_numbers = set()
    while number_pointer < len(numbers):
        current_numbers.add(numbers[number_pointer])
        for board in boards:
            if has_won(current_numbers, board):
                if len(boards) == 1:
                    return sum(sum(n for n in row if n not in current_numbers) for row in board)*numbers[number_pointer]
                boards.remove(board)
        number_pointer += 1

if __name__ == "__main__":
    bingo = open("input.txt").read().strip().split("\n\n")
    numbers = [int(n) for n in bingo[0].split(",")]
    boards = [[[int(n) for n in row.split()] for row in board.split("\n")] for board in bingo[1:]]
    print(find_winner_score(numbers, boards))

