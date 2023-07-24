def increment(scanners, size, pos, desc):
    if desc:
        if pos+1 >= size:
            desc = False
            pos -= 1
        else:
            pos += 1
    else:
        if pos-1 < 0:
            desc = True
            pos += 1
        else:
            pos -= 1
    scanners[id][3] = desc
    scanners[id][2] = pos


if __name__ == "__main__":
    scanners = [[int(i) for i in s.split(": ")] + [0, True] for s in open("input.txt").read().strip().split("\n")]

    for id in range(len(scanners)):
        depth, size, pos, desc = scanners[id]
        for _ in range(depth):
            increment(scanners, size, pos, desc)
            depth, size, pos, desc = scanners[id]

    delay = 0

    while any(s[2] == 0 for s in scanners):
        for id in range(len(scanners)):
            depth, size, pos, desc = scanners[id]
            increment(scanners, size, pos, desc)
        delay += 1

    print(delay)
        
    
