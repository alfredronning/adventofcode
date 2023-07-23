if __name__ == "__main__":
    rows = [[int(d) for d in row.split()] for row in open("input.txt").read().strip().split("\n")]

    print(sum(max(row)-min(row) for row in rows))
