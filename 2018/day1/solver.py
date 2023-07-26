if __name__ == "__main__":
    frequencies = open("input.txt").read().strip().split("\n")
    print(sum(int(i) for i in frequencies))

