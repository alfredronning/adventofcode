def find_extrapolated_value(seq):
    extrapolated = [seq]
    while True:
        last = extrapolated[-1]
        if all(i == 0 for i in last):
            break
        extrapolated.append([last[i+1]-last[i] for i in range(0, len(last)-1)])
    for i in range(1, len(extrapolated)):
        new_val = extrapolated[-i-1][0]-extrapolated[-i][0]
        extrapolated[-i-1] = [new_val] + extrapolated[-i-1]
    return extrapolated[0][0]

if __name__ == "__main__":
    seqs = [[int(i) for i in s.split()] for s in open("testinput.txt").read().strip().split("\n")]
    res = 0
    for seq in seqs:
        res += find_extrapolated_value(seq)
    print(res)

