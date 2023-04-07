if __name__ == "__main__":
    start, stop = [int(i) for i in open("input.txt").read().strip().split("-")]
    count = 0
    for i in range(start, stop+1):
        s = str(i)
        if "".join(sorted(s)) != s:
            continue
        if 2 in [s.count(str(j)) for j in range(10)]:
            count += 1
    print(count)

