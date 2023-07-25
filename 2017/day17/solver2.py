if __name__ == "__main__":
    step = 356

    buffer = 1
    pos = 0
    after_0 = 0
    for i in range(1, 50_000_001):
        endpos = (pos+step)%buffer
        buffer += 1
        if endpos == 0:
            after_0 = i
        pos = endpos+1
    print(after_0)

