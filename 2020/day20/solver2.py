def find_pattern(img):
    pattern = []
    pattern.append(img[0])
    pattern.append(img[-1])
    pattern.append([row[0] for row in img])
    pattern.append([row[-1] for row in img])
    return pattern

def get_all_orientations(img):
    res = []
    # normal and mirrored
    res.append(img)
    res.append([row[::-1] for row in img])
    # 90 degrees clockwise and mirrored
    res.append([[img[i][j] for i in range(len(img))][::-1] for j in range(len(img[0]))])
    res.append([[img[i][j] for i in range(len(img))] for j in range(len(img[0]))])
    # 180 degrees clockwise and mirrored
    res.append([row[::-1] for row in img[::-1]])
    res.append(img[::-1])
    # 270 degrees clockwise and mirrored
    res.append([[img[i][j] for i in range(len(img))] for j in range(len(img[0]))][::-1])
    res.append([[img[::-1][i][j] for i in range(len(img))] for j in range(len(img[0]))][::-1])
    return res

def assmeble_img(img_dict, pattern_dict):
    dimension = int(len(img_dict)**0.5)
    images = [[None]*dimension for _ in range(dimension)]
    placed = set()

    # find first corner (has only two neighbours), orient it correctly, and use as 0,0
    for title in img_dict:
        neighbours = []
        for orientation, pattern in enumerate(pattern_dict[title]):
            for other in img_dict:
                if title == other:
                    continue
                if pattern in pattern_dict[other]+[p[::-1] for p in pattern_dict[other]]:
                    neighbours.append(pattern)
                    break
        if len(neighbours) == 2:
            placed.add(title)
            for image_oriented in get_all_orientations(img_dict[title])[::-1]:
                bottomleft_edges = [image_oriented[-1], image_oriented[-1][::-1],
                                    [row[-1] for row in image_oriented], [row[-1] for row in image_oriented][::-1]]
                if sum(bottomleft_edge in neighbours for bottomleft_edge in bottomleft_edges) == 2:
                    images[0][0] = image_oriented
                    break
            break

    # find the first row from the corner
    right_side_pattern = [row[-1] for row in images[0][0]]
    col = 1
    while images[0][-1] is None:
        for other in img_dict:
            if other in placed:
                continue
            for other_oriented in get_all_orientations(img_dict[other]):
                left_side_pattern_other = [row[0] for row in other_oriented]
                if left_side_pattern_other == right_side_pattern:
                    images[0][col] = other_oriented
                    right_side_pattern = [row[-1] for row in other_oriented]
                    col += 1
                    placed.add(other)
                    break

    # use the first row to draw out all the columns
    for col in range(dimension):
        current = images[0][col]
        bottom_side_pattern = current[-1]
        row = 1
        while images[-1][col] is None:
            for other in img_dict:
                if other in placed:
                    continue
                for other_oriented in get_all_orientations(img_dict[other]):
                    top_side_pattern_other = other_oriented[0]
                    if top_side_pattern_other == bottom_side_pattern:
                        images[row][col] = other_oriented
                        bottom_side_pattern = other_oriented[-1]
                        row += 1
                        placed.add(other)
                        break
    return images

def crop_image(images):
    cropped_rows = []
    for row in images:
        for img_row in range(1, len(row[0])-1):
            current_row = []
            for img in row:
                current_row += img[img_row][1:-1]
            cropped_rows.append(current_row)
    return cropped_rows

def get_dragon_pixels(lit_pixels, height, width):
    dragon = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]
    overlapping_dragon_pixels = set()
    for dragon_oriented in get_all_orientations(dragon):
        current_dragon_pixels = set()
        for dragon_row in range(len(dragon_oriented)):
            for dragon_col in range(len(dragon_oriented[0])):
                if dragon_oriented[dragon_row][dragon_col]:
                    current_dragon_pixels.add((dragon_row, dragon_col))
        for row in range(height):
            for col in range(width):
                if all((row+d_pixel[0], col+d_pixel[1]) in lit_pixels for d_pixel in current_dragon_pixels):
                    for d_pixel in current_dragon_pixels:
                        overlapping_dragon_pixels.add((row+d_pixel[0], col+d_pixel[1]))
    return overlapping_dragon_pixels

if __name__ == "__main__":
    images = open("input.txt").read().strip().split("\n\n")
    img_dict = dict()
    pattern_dict = dict()
    for img in images:
        img = img.split("\n")
        title = int(img[0].split()[1][:-1])
        img = [[1 if pixel == "#" else 0 for pixel in row] for row in img[1:]]
        img_dict[title] = img
        pattern_dict[title] = find_pattern(img)

    assembled = assmeble_img(img_dict, pattern_dict)
    cropped = crop_image(assembled)
    lit_pixels = set()
    for i, row in enumerate(cropped):
        for j, pixel in enumerate(row):
            if pixel:
                lit_pixels.add((i, j))
    height, width = len(cropped), len(cropped[0])

    dragon_pixels = get_dragon_pixels(lit_pixels, height, width)
    print(sum(pixel not in dragon_pixels for pixel in lit_pixels))
