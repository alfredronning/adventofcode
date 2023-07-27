def find_length(inp):
    recipees = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        new_recipee = str(recipees[elf1]+recipees[elf2])
        for c in new_recipee:
            recipees.append(int(c))
            if "".join(str(s) for s in recipees[-len(inp):]) == inp:
                return len(recipees)-len(inp)
        elf1 = (elf1 + 1 + recipees[elf1]) % len(recipees)
        elf2 = (elf2 + 1 + recipees[elf2]) % len(recipees)


if __name__ == "__main__":
    inp = "147061"
    print(find_length(inp))

