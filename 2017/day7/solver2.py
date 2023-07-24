def calc_weight(tree, program):
    weight, hold_up = tree[program]
    for c in hold_up:
        weight += calc_weight(tree, c)
    return weight


def balance_branch(tree, program, diff):
    weight, hold_up = tree[program]
    hold_up_weights = [calc_weight(tree, n) for n in hold_up]
    if len(set(hold_up_weights)) == 1:
        tree[program] = (weight-diff, hold_up)
        print(program)
        print(tree[program])
        return
    correct = 0
    wrong = 0
    wrong_index = 0
    for i in range(len(hold_up_weights)):
        current = hold_up_weights[i]
        if hold_up_weights.count(current) == 1:
            wrong = current
            wrong_index = i
        else:
            correct = current
    balance_branch(tree, hold_up[wrong_index], wrong-correct)


if __name__ == "__main__":
    program_list = open("input.txt").read().strip().split("\n")

    tree = {}
    non_root = set()
    is_balanced = {}

    for program_line in program_list:
        program = program_line.split(" -> ")[0]
        hold_up = program_line.split(" -> ")[1].split(", ") if " -> " in program_line else []
        program_name, program_weight = program.replace("()", "").split()
        tree[program_name] = (int(program_weight[1:-1]), hold_up)
        is_balanced[program_name] = False
        for p in hold_up:
            non_root.add(p)

    root = None
    for p in tree:
        if p not in non_root:
            root = p
            break

    balance_branch(tree, root, 0)

