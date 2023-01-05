def tree_visible(woods, row, col):
    current = woods[row][col]
    if all(tree < current for tree in woods[row][:col]):
        return True
    if all(tree < current for tree in woods[row][col+1:]):
        return True
    if all(woods[i][col] < current for i in range(row)):
        return True
    if all(woods[i][col] < current for i in range(row+1, len(woods))):
        return True
    return False

if __name__ == "__main__":
    visible = 0
    woods = open("input.txt").read().strip().split("\n")
    for row in range(len(woods)):
        for col in range(len(woods[0])):
            if tree_visible(woods, row, col):
                visible += 1
    print(visible)

