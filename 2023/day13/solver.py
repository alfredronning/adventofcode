def is_symetric_horizontal(pattern, x):
    checksize = min(x, len(pattern)-x)
    for i in range(checksize):
        for j in range(len(pattern[0])):
            if pattern[x-i-1][j] != pattern[x+i][j]:
                return False
    return True

def is_symetric_vertical(pattern, x):
    checksize = min(x, len(pattern[0])-x)
    for i in range(checksize):
        for j in range(len(pattern)):
            if pattern[j][x-i-1] != pattern[j][x+i]:
                return False
    return True

def calc_pattern(pattern):
    rows = 0
    cols = 0
    while not is_symetric_horizontal(pattern, rows+1):
       rows += 1
    if rows < len(pattern)-1:
        return (rows+1)*100
    while not is_symetric_vertical(pattern, cols+1):
       cols += 1
    return cols+1

if __name__ == "__main__":
    patterns = [p.split("\n") for p in open("input.txt").read().strip().split("\n\n")]
    res = 0
    for pattern in patterns:
        res += calc_pattern(pattern)
    print(res)

