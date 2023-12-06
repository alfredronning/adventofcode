if __name__ == "__main__":
    t, d = [int(j.split(":")[1].replace(" ", "")) for j in open("input.txt").read().strip().split("\n")]
    ways = 0
    for press in range(t):
        if press * (t-press) > d:
            ways += 1
    print(ways)

