if __name__ == "__main__":
    initial_state, notes = open("input.txt").read().strip().split("\n\n")
    initial_state = [".", ".", "."]+[c for c in initial_state.split(": ")[1]]+[".", ".", "."]
    generations = 20

    zero_index = 3

    rules = {}
    for rule in notes.split("\n"):
        state, to = rule.split(" => ")
        rules[state] = to

    for _ in range(generations):
        initial_state = initial_state
        next_state = ["." for _ in range(len(initial_state)+2)]
        for i in range(2, len(initial_state)-2):
            current_span = "".join(initial_state[i-2:i+3])
            if current_span in rules:
                next_state[i+1] = rules[current_span]
            else:
                next_state[i+1] = "."
        initial_state = next_state
        zero_index += 1
    score = 0
    for i, c in enumerate(initial_state):
        if c == "#":
            score += i-zero_index
    print(score)

