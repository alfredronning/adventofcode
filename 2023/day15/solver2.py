def calc_hash(s):
    current = 0
    for c in s:
        o = ord(c)
        current += o
        current *= 17
        current &= 0b11111111
    return current

if __name__ == "__main__":
    steps = open("input.txt").read().strip().split(",")
    boxes = [dict() for _ in range(256)]
    for step in steps:
        if "=" in step:
            op = "="
        else:
            op = "-"
        label, value = step.split(op)
        h = calc_hash(label)
        if op == "=":
            boxes[h][label] = value
        else:
            boxes[h].pop(label, None)
    res = 0
    for i, box in enumerate(boxes):
        for j, v in enumerate(box.values()):
            res += int(v)*(i+1)*(j+1)
    print(res)


