import re

if __name__ == "__main__":
    json = open("input.txt").read().strip()
    res = 0
    for n in re.findall("-?[0-9]+", json):
        res += int(n)
    print(res)

