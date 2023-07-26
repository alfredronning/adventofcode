from re import findall

def simulate(points):
    p_set = set()
    min_x = min_y = float("inf")
    max_x = max_y = 0
    for p, v in points:
        p[0] += v[0]
        p[1] += v[1]

        p_set.add(tuple(p))
        min_x = min(min_x, p[0])
        min_y = min(min_y, p[1])
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])
    return p_set, min_x, max_x, min_y, max_y

def print_img(p_set, min_x, max_x, min_y, max_y):
    print("--------------------------------------")
    for i in range(min_y, max_y+1):
        row = ""
        for j in range(min_x, max_x+1):
            if (j, i) in p_set:
                row += "#"
            else:
                row += "."
        print(row)
    print("--------------------------------------")

if __name__ == "__main__":
    notes = open("input.txt").read().strip().split("\n")
    img_size = 65
    points = []
    min_x = min_y = float("inf")
    max_x = max_y = 0
    p_set = set()
    for n in notes:
        p, v = findall(r"<[^<]*>", n)
        p = [int(i) for i in p[1:-1].split(",")]
        v = [int(i) for i in v[1:-1].split(",")]
        points.append((p, v))

        p_set.add(tuple(p))
        min_x = min(min_x, p[0])
        min_y = min(min_y, p[1])
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])

    for i in range(1, 20000):
        p_set, min_x, max_x, min_y, max_y = simulate(points)
        if max_x-min_x <= img_size and max_y-min_y <= img_size:
            print(i)
            print_img(p_set, min_x, max_x, min_y, max_y)

