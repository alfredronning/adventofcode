if __name__ == "__main__":
    moves = open("input.txt").read().strip().split(",")
    start = "abcdefghijklmnop"
    programs = [c for c in start]
    runs = 1_000_000_000

    i = 0
    while i < runs:
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

        i += 1
        if "".join(programs) == start:
            i = runs//i*i
    print("".join(programs))

