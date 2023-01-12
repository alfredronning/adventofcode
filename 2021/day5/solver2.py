if __name__ == "__main__":
    lines = open("input.txt").read().strip().split("\n")

    covered = set()
    double_covered = set()
    count = 0
    for line in lines:
        start, end = line.split(" -> ")
        start, end = [int(i) for i in start.split(",")], [int(i) for i in end.split(",")]
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1])+1):
                current = start[0], i
                if current in covered:
                    double_covered.add(current)
                else:
                    covered.add(current)
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
                current = i, start[1]
                if current in covered:
                    double_covered.add(current)
                else:
                    covered.add(current)
        else:
            direction = 1 if end[0] > start[0] else -1, 1 if end[1] > start[1] else -1
            for i in range(abs(end[0]-start[0])+1):
                current = start[0]+i*direction[0], start[1]+i*direction[1]
                if current in covered:
                    double_covered.add(current)
                else:
                    covered.add(current)
    print(len(double_covered))

