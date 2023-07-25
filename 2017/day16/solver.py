if __name__ == "__main__":
    moves = open("input.txt").read().strip().split(",")
    programs = [c for c in "abcdefghijklmnop"]

    for move in moves:
        if move[0] == "s":
            for _ in range(int(move[1:])):
                programs = [programs[-1]] + programs[:-1]
        elif move[0] == "x":
            a, b = move[1:].split("/")
            tmp = programs[int(a)]
            programs[int(a)] = programs[int(b)]
            programs[int(b)] = tmp
        elif move[0] == "p":
            a, b = move[1:].split("/")
            a, b = programs.index(a), programs.index(b)
            tmp = programs[int(a)]
            programs[int(a)] = programs[int(b)]
            programs[int(b)] = tmp

    print("".join(programs))

