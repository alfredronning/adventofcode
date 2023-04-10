def increment_pw(pw):
    index = 7
    while index >= 0:
        if pw[index] != "z":
            if chr(ord(pw[index])+1) in "iol":
                pw[index] = chr(ord(pw[index])+2)
            else:
                pw[index] = chr(ord(pw[index])+1)
            return pw
        pw[index] = "a"
        index -= 1
    return pw
    
def valid_pw(pw):
    three_straight_increasing = False
    for i in range(6):
        one, two, three = ord(pw[i]), ord(pw[i+1]), ord(pw[i+2])
        if three == two+1 and two == one+1:
            three_straight_increasing = True
            break
    if not three_straight_increasing:
        return False
    for c in pw:
        if c in "iol":
            return False
    overlapping = 0
    i = 0
    while i <= 6:
        if pw[i] == pw[i+1]:
            overlapping += 1
            i+=2
        else:
            i+=1
    return overlapping >= 2

if __name__ == "__main__":
    pw = [i for i in "cqjxxyzz"]
    while True:
        pw = increment_pw(pw)
        if valid_pw(pw):
            break
    print("".join(pw))

