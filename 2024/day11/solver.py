inp = [int(i) for i in open("input.txt").read().strip().split()]

cache = dict()

def get_after_i(n, i, c):
    if i == 0:
        return 1
    if (n, i) in c:
        return c[(n, i)]
    si = str(n)
    if n == 0:
        res = get_after_i(1, i-1, c)
    elif len(si)%2 == 0:
        res = get_after_i(int(si[len(si)//2:]), i-1, c) + get_after_i(int(si[:len(si)//2]), i-1, c)
    else:
        res = get_after_i(n*2024, i-1, c)
    c[n, i] = res
    return res

print(sum(get_after_i(i, 25, cache) for i in inp))
print(sum(get_after_i(i, 75, cache) for i in inp))

