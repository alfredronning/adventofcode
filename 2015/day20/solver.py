from collections import defaultdict

def find_best(sumnums, bound):
    houses = defaultdict(int)
    for i in range(1, bound):
        if houses[i] + i >= sumnums:
            return i
        for j in range(i, bound, i):
            houses[j] += i
    return find_best(sumnums, bound*2)

if __name__ == "__main__":
    target = 33_100_000
    inp = target//10
    print(find_best(inp, 1))

