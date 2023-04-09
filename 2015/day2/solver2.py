if __name__ == "__main__":
    presents = open("input.txt").read().strip().split("\n")
    ribbon = 0
    for present in presents:
        l, w, h = sorted([int(i) for i in present.split("x")])
        ribbon += l+l+w+w+l*w*h
    print(ribbon)

