if __name__ == "__main__":
    coords = [tuple(int(i) for i in c.split(", ")) for c in open("input.txt").read().strip().split("\n")]
    x, y = list(zip(*coords))
    min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)
    max_sum = 10000

    region_size = 0

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            dists = [abs(i-c[0])+abs(j-c[1]) for c in coords]
            if sum(dists) < max_sum:
                region_size += 1
    print(region_size)

