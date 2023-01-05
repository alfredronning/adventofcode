def parse_input(filename):
    creates, moves = open(filename).read().split("\n\n")
    creates, moves = creates.split("\n"), moves.strip().split("\n")
    stacks = [[] for _ in range(len(creates[-1].split()))]
    for row in creates[:-1]:
        for i in range(1, len(row), 4):
            if row[i].isalpha():
                stacks[(i-1)//4].append(row[i])
    moves = [[c for c in move.split() if c.isdigit()] for move in moves]
    return stacks, moves

def move_creates(stacks, move):
    amount, from_stack, to_stack = move
    amount, from_stack, to_stack = int(amount), int(from_stack)-1, int(to_stack)-1
    stacks[to_stack] = stacks[from_stack][:amount] + stacks[to_stack]
    stacks[from_stack] = stacks[from_stack][amount:]


if __name__ == "__main__":
    stacks, moves = parse_input("input.txt")
    for move in moves:
        move_creates(stacks, move)
    print("".join(stack[0] for stack in stacks))


