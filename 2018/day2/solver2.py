def find_one_diff(boxes):
    for box in boxes:
        for other_box in boxes:
            diff_letters = []
            for i in range(len(box)):
                if box[i] != other_box[i]:
                    diff_letters.append((box[i], i))
            if len(diff_letters) == 1:
                return box[:diff_letters[0][1]] + box[diff_letters[0][1]+1:]


if __name__ == "__main__":
    boxes = open("input.txt").read().strip().split("\n")
    print(find_one_diff(boxes))

