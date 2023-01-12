POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
MATCHING = {"(": ")", "[": "]", "{": "}", "<": ">"}

def find_score(inp):
    openingtags = []
    res = 0
    for tag in inp:
        if tag in "([{<":
            openingtags.append(tag)
        else:
            matcing_tag = MATCHING[openingtags.pop()]
            if tag != matcing_tag:
                res += POINTS[tag]
    return res

if __name__ == "__main__":
    inputs = open("input.txt").read().strip().split("\n")
    res = 0
    for inp in inputs:
        res += find_score(inp)
    print(res)

