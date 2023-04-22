from collections import defaultdict

def find_best(sumnums):
    houses = defaultdict(int)
    for i in range(1, sumnums):
        if houses[i] + i >= sumnums:
            return i
        for j in range(i, i*50, i):
            houses[j] += i

if __name__ == "__main__":
    target = 33_100_000
    inp = target//11
    print(find_best(inp))

