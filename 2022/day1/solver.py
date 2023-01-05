if __name__ == "__main__":
    max_cal = 0
    for elf in open("input.txt").read().split("\n\n"):
        max_cal = max(sum(int(row) for row in elf.strip().split("\n")), max_cal)
    print(max_cal)

