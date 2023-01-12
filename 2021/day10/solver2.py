POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
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
                return 0
    for closingtag in [MATCHING[openingtag] for openingtag in openingtags][::-1]:
        res = res*5 + POINTS[closingtag]
    return res

if __name__ == "__main__":
    inputs = open("input.txt").read().strip().split("\n")
    res = [find_score(inp) for inp in inputs]
    res = sorted([n for n in res if n != 0])
    print(res[len(res)//2])

