from collections import defaultdict

if __name__ == "__main__":
    claims = open("input.txt").read().strip().split("\n")
    inch_claims = defaultdict(int)
    for claim in claims:
        id, dimensions = claim.split(" @ ")
        offset, size = dimensions.split(": ")
        o_x, o_y = [int(i) for i in offset.split(",")]
        s_x, s_y = [int(i) for i in size.split("x")]
        for i in range(o_x, o_x+s_x):
            for j in range(o_y, o_y+s_y):
                inch_claims[(i, j)] += 1
    print(len([i for i in inch_claims.values() if i > 1]))
            
