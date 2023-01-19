if __name__ == "__main__":
    groups = open("input.txt").read().strip().split("\n")
    print(sum(len(set(grp.replace("\n", ""))) for grp in groups))

