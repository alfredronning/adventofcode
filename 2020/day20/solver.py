def find_pattern(img):
    pattern = []
    pattern.append(img[0])
    pattern.append(img[-1])
    pattern.append([row[0] for row in img])
    pattern.append([row[-1] for row in img])
    return pattern

def find_corners(img_dict, pattern_dict):
    res = 1
    for title in img_dict:
        neighbours = 0
        for pattern in pattern_dict[title]:
            for other in img_dict:
                if title == other:
                    continue
                if pattern in pattern_dict[other]+[p[::-1] for p in pattern_dict[other]]:
                    neighbours += 1
                    break
        if neighbours == 2:
            res *= title
    return res

if __name__ == "__main__":
    images = open("testinput.txt").read().strip().split("\n\n")
    img_dict = dict()
    pattern_dict = dict()
    for img in images:
        img = img.split("\n")
        title = int(img[0].split()[1][:-1])
        img = [[1 if pixel == "#" else 0 for pixel in row] for row in img[1:]]
        img_dict[title] = img
        pattern_dict[title] = find_pattern(img)
    print(find_corners(img_dict, pattern_dict))
