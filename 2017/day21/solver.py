def enhance(pattern, rules):
    next_pattern = []
    pixel_size = 3 if len(pattern)%2 else 2
    for i in range(len(pattern)//pixel_size):
        for _ in range(pixel_size+1):
            next_pattern.append([])
        for j in range(len(pattern)//pixel_size):
            current_pixel = [row[j*pixel_size:(j+1)*pixel_size] for row in pattern[i*pixel_size:(i+1)*pixel_size]]
            transformed_pixel = rules["/".join("".join(c for c in r) for r in current_pixel)].split("/")
            for k in range(pixel_size+1):
                next_pattern[i*(pixel_size+1)+k] += [c for c in transformed_pixel[k]]
    return next_pattern

def get_flips(pixel):
    pixel = [[c for c in row] for row in pixel.split("/")]
    flips = []
    for _ in range(3):
        flips.append("/".join("".join(r) for r in pixel))
        flips.append("/".join("".join(r[::-1]) for r in pixel))
        pixel = [[pixel[j][i] for j in range(len(pixel))] for i in range(len(pixel[0])-1,-1,-1)]
    return flips

if __name__ == "__main__":
    rules = dict(r.split(" => ") for r in open("input.txt").read().strip().split("\n"))
    for rule in list(rules):
        transform = rules[rule]
        flips = get_flips(rule)
        for flip in flips:
            rules[flip] = transform

    pattern = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]

    for _ in range(18):
        pattern = enhance(pattern, rules)

    print(sum(r.count("#") for r in pattern))

