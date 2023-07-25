if __name__ == "__main__":
    step = 356

    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        endpos = (pos+step)%len(buffer)
        buffer.insert(endpos+1, i)
        pos = endpos+1
    print(buffer[1])

