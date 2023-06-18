if __name__ == "__main__":
    messages = open("input.txt").read().strip().split("\n")
    res = ""
    for i in range(len(messages[0])):
        col = "".join(row[i] for row in messages)
        counts = [(-col.count(c), c) for c in list(set(col))]
        res += sorted(counts)[-1][1]
    print(res)

