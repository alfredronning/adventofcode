if __name__ == "__main__":
    presents = open("input.txt").read().strip().split("\n")
    area = 0
    for present in presents:
        l, w, h = sorted([int(i) for i in present.split("x")])
        area += 3*l*w+2*l*h+2*w*h
    print(area)

