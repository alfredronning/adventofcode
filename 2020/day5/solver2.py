if __name__ == "__main__":
    b_passes = open("input.txt").read().strip().split("\n")
    taken = set()
    for b in b_passes:
        taken.add(int("".join("1" if i=="B" else "0" for i in b[:7]),2)*8+int("".join("1" if i=="R" else "0" for i in b[7:]),2))
    seatid = 16
    while seatid in taken:
        seatid += 1
    print(seatid)

