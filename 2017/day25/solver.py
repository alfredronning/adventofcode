if __name__ == "__main__":
    blueprints = open("input.txt").read().strip().replace(".", "").replace(":", "").split("\n\n")
    current_state = blueprints[0].split("\n")[0].split()[-1]
    checksum = int(blueprints[0].split("\n")[1].split()[-2])

    state_actions = {}
    for blueprint in blueprints[1:]:
        actions = blueprint.split("\n")
        state = actions[0].split()[-1]
        zero_actions = (int(actions[2].split()[-1]), actions[3].split()[-1], actions[4].split()[-1])
        one_actions = (int(actions[6].split()[-1]), actions[7].split()[-1], actions[8].split()[-1])
        state_actions[state] = (zero_actions, one_actions)

    cursor = 0
    tape = {0: 0}

    for _ in range(checksum):
        zero_actions, one_actions = state_actions[current_state]
        if tape[cursor] == 0:
            write_val, move, next_state = zero_actions
        else:
            write_val, move, next_state = one_actions
        tape[cursor] = write_val
        cursor += 1 if move == "right" else -1
        if cursor not in tape:
            tape[cursor] = 0
        current_state = next_state

    print(sum(tape.values()))

