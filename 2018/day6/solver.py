if __name__ == "__main__":
    coords = [tuple(int(i) for i in c.split(", ")) for c in open("input.txt").read().strip().split("\n")]
    x, y = list(zip(*coords))
    min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)

    closest = {}
    infinites = set()
    for x in range(min_x, max_x+1):
        left, right = (x, min_y), (x, max_y)
        left_dists = [abs(left[0]-c[0])+abs(left[1]-c[1]) for c in coords]
        right_dists = [abs(right[0]-c[0])+abs(right[1]-c[1]) for c in coords]
        left_min = min(left_dists)
        right_min = min(right_dists)
        if left_dists.count(left_min) == 1:
            infinites.add(left_dists.index(left_min))
        if right_dists.count(right_min) == 1:
            infinites.add(right_dists.index(right_min))

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            dists = [abs(i-c[0])+abs(j-c[1]) for c in coords]
            min_dist = min(dists)
            if dists.count(min_dist) == 1:
                c = dists.index(min_dist)
                if c not in closest:
                    closest[c] = 1
                else:
                    closest[c] += 1

    largest = max(closest[c] for c in range(len(coords)) if c not in infinites)
    print(largest)

