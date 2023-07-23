if __name__ == "__main__":
    rows = [sorted([int(d) for d in row.split()])[::-1] for row in open("input.txt").read().strip().split("\n")]

    res = 0
    for row in rows:
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if row[i]/row[j] == row[i]//row[j]:
                    res += row[i]//row[j]
    print(res)
        
