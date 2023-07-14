def get_dragon_curve(start, length):
    while len(start) < length:
        start = start + "0" + "".join("1" if i == "0" else "0" for i in start)[::-1]
    return start

def calc_checksum(data):
    while len(data)%2 == 0:
        data = "".join("1" if data[i*2] == data[i*2+1] else "0" for i in range(len(data)//2))
    return data

if __name__ == "__main__":
    inp = "10011111011011001"
    length = 35651584

    data = get_dragon_curve(inp, length)[:length]
    print(calc_checksum(data))
    
