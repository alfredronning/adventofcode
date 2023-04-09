def is_nice(s):
    if len([i for i in s if i in "aeiou"]) < 3:
        return False
    if any(sub_s in s for sub_s in ["ab", "cd", "pq", "xy"]):
        return False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

if __name__ == "__main__":
    strings = open("input.txt").read().strip().split("\n")
    count = 0
    for s in strings:
        count += is_nice(s)
    print(count)

