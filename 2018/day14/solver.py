if __name__ == "__main__":
    inp = 147061

    recipees = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipees) <= inp+10:
        new_recipee = str(recipees[elf1]+recipees[elf2])
        for c in new_recipee:
            recipees.append(int(c))
        elf1 = (elf1 + 1 + recipees[elf1]) % len(recipees)
        elf2 = (elf2 + 1 + recipees[elf2]) % len(recipees)

    print("".join(str(s) for s in recipees[inp:inp+10]))

