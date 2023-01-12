def fold(points, folding_y, index):
    if folding_y:
        first = {point for point in points if point[1]< index}
        second = {point for point in points if point[1] >= index}
        for point in second:
            first.add((point[0], 2*index - point[1]))
    else:
        first = {point for point in points if point[0] < index}
        second = {point for point in points if point[0] >= index}
        for point in second:
            first.add((2*index - point[0], point[1]))
    return first

if __name__ == "__main__":
    points, instructions = open("input.txt").read().strip().split("\n\n")
    points = {tuple(int(coord) for coord in point.split(",")) for point in points.split("\n")}
    instructions = [(True if "y" in instruction else False, int(instruction.split("=")[1])) for instruction in instructions.strip().split("\n")]
    for folding_y, index in instructions[:1]:
        points = fold(points, folding_y, index)
    print(len(points))
