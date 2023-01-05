def calc_score(woods, row, col):
    current = woods[row][col]
    score = 1
    see_throught = True
    for i, tree in enumerate(woods[row][:col][::-1]):
        if tree >= current:
            see_throught = False
            score *= i+1
            break
    if see_throught:
        score *= max(1, col)
    see_throught = True
    for i, tree in enumerate(woods[row][col+1:]):
        if tree >= current:
            see_throught = False
            score *= i+1
            break
    if see_throught:
        score *= max(1, len(woods[0])-col-1)
    see_throught = True
    for i in range(1, row+1):
        if woods[row-i][col] >= current:
            see_throught = False
            score *= i
            break
    if see_throught:
        score *= max(1, row)
    see_throught = True
    for i in range(1, len(woods)-row):
        if woods[row+i][col] >= current:
            see_throught = False
            score *= i
            break
    if see_throught:
        score *= max(1, len(woods)-row-1)
    return score

if __name__ == "__main__":
    best_score = 0
    woods = open("input.txt").read().strip().split("\n")
    for row in range(len(woods)):
        for col in range(len(woods[0])):
            score = calc_score(woods, row, col)
            print(row, col, score)
            if score > best_score:
                best_score = score
    print(best_score)

