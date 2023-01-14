def enhance(img, enhance_alg, pad):
    padded = [[pad]*2 + row + [pad]*2 for row in img]
    padded = [[pad]*len(padded[0])]*2 + padded + [[pad]*len(padded[0])]*2
    enhanced = [["0"]*(len(img[0])+2) for _ in range(len(img)+2)]
    for i in range(len(enhanced)):
        for j in range(len(enhanced[0])):
            conv = ""
            for conv_i in range(-1, 2):
                for conv_j in range(-1, 2):
                    conv += padded[i+1+conv_i][j+1+conv_j]
            decimal = int(conv, 2)
            if enhance_alg[decimal]:
                enhanced[i][j] = "1"
    return enhanced

if __name__ == "__main__":
    enhance_alg, img = open("input.txt").read().strip().split("\n\n")
    enhance_alg = [True if i == "#" else False for i in enhance_alg]
    img = [["1" if pixel == "#" else "0" for pixel in row] for row in img.split("\n")]
    for i in range(50):
        if not enhance_alg[0]:
            pad = "0"
        elif enhance_alg[-1]:
            pad = "0" if i == 0 else "1"
        else:
            pad = "1" if i % 2 else "0"
        img = enhance(img, enhance_alg, pad)
    print(sum(row.count("1") for row in img))

