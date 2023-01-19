if __name__ == "__main__":
    b_passes = open("input.txt").read().strip().split("\n")
    print(max(int("".join("1" if i=="B" else "0" for i in b[:7]),2)*8+int("".join("1" if i=="R" else "0" for i in b[7:]),2) for b in b_passes))

