import re

if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    inp = re.sub("!.", "", inp)
    
    count = 0
    in_garbage = False

    for c in inp:
        if in_garbage:
            if c == ">":
                in_garbage = False
            else:
                count += 1
        else:
            if c == "<":
                in_garbage = True
    print(count)

