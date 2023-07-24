import re

if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    inp = re.sub("!.", "", inp)
    inp = re.sub("<[^>]*>", "<g>", inp)
    
    depth = 0
    score = 0

    for c in inp:
        if c == "{":
            depth += 1
        elif c == "}":
            score += depth
            depth -= 1

    print(score)


