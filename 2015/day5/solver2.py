def is_nice(s):
    got_repeating = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            got_repeating = True
            break
    if not got_repeating:
        return False
    for i in range(len(s)-1):
        if s.count(s[i:i+2]) > 1:
            return True
    return False

if __name__ == "__main__":
    strings = open("input.txt").read().strip().split("\n")
    count = 0
    for s in strings:
        count += is_nice(s)
    print(count)

