def look_and_say(inp):
    current_num = inp[0]
    count = 1
    i = 1
    res = ""
    while i < len(inp):
        next_num = inp[i]
        if next_num == current_num:
            count += 1
        else:
            res += str(count)+current_num
            current_num = next_num
            count = 1
        i += 1
    res += str(count)+current_num
    return res

if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    for _ in range(50):
        inp = look_and_say(inp)
    print(len(inp))

