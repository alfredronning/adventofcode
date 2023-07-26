from collections import defaultdict

def none_overlap(inch_claims, claims):
    _, dimensions = claim.split(" @ ")
    offset, size = dimensions.split(": ")
    o_x, o_y = [int(i) for i in offset.split(",")]
    s_x, s_y = [int(i) for i in size.split("x")]
    for i in range(o_x, o_x+s_x):
        for j in range(o_y, o_y+s_y):
            if inch_claims[(i, j)] != 1:
                return False
    return True


if __name__ == "__main__":
    claims = open("input.txt").read().strip().split("\n")
    inch_claims = defaultdict(int)
    for claim in claims:
        _, dimensions = claim.split(" @ ")
        offset, size = dimensions.split(": ")
        o_x, o_y = [int(i) for i in offset.split(",")]
        s_x, s_y = [int(i) for i in size.split("x")]
        for i in range(o_x, o_x+s_x):
            for j in range(o_y, o_y+s_y):
                inch_claims[(i, j)] += 1
    for claim in claims:
        if none_overlap(inch_claims, claims):
            print(claim.split(" @ ")[0][1:])
            break

