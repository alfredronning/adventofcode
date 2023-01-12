if __name__ == "__main__":
    entries = sum((entry.split(" | ")[1].split() for entry in open("input.txt").read().strip().split("\n")), [])
    res = sum(len(set(entry)) in [2, 3, 4, 7] for entry in entries)
    print(res)

