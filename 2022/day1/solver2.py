if __name__ == "__main__":
    elfs = open("input.txt").read().split("\n\n")
    elf_cals = sorted([sum(int(row) for row in elf.strip().split("\n")) for elf in elfs])
    print(sum(elf_cals[-3:]))

