def find_next_row(row):
    row = [1]+row+[1]
    next_row = []
    for i in range(1, len(row)-1):
        left, center, right = row[i-1], row[i], row[i+1]
        if not left and not center and right:
            next_row.append(0)
        elif left and not center and not right:
            next_row.append(0)
        elif not left and center and right:
            next_row.append(0)
        elif left and center and not right:
            next_row.append(0)
        else:
            next_row.append(1)
    return next_row

if __name__ == "__main__":
    current_row = [1 if c == "." else 0 for c in open("input.txt").read().strip()]
    room = [current_row]
    rows = 400000
    res = sum(current_row)
    for i in range(rows-1):
        current_row = find_next_row(current_row)
        res += sum(current_row)
    print(res)

