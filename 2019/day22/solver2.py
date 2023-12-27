def mat_mult(m1, m2, mod):
    res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            acc = 0
            for k in range(len(m1[0])):
                acc += m1[i][k] * m2[k][j]
            if mod != 0:
                acc %= mod
            res[i][j] = acc
    return res

def mat_pow(m, exp, mod=0):
    res = [[1, 0], [0, 1]]
    while exp > 0:
        if exp % 2 == 1:
            res = mat_mult(res, m, mod)
        m = mat_mult(m, m, mod)
        exp //= 2
    return res

def get_at_position(techniques, cards, times, position):
    a = 1
    b = 0
    for technique in techniques:
        if technique == "deal into new stack":
            a *= -1
            b = -b-1
        if "cut" in technique:
            n = int(technique.split()[-1])
            b -= n
        elif "deal with increment" in technique:
            n = int(technique.split()[-1])
            a *= n
            b *= n
    a = a % cards
    b = b % cards
    a = pow(a, cards-2, cards)
    b = (-b*a)%cards
    m = [[a, b], [0, 1]]
    m = mat_pow(m, times, cards)
    m = mat_mult(m, [[position], [1]], cards)
    return m[0][0]

if __name__ == "__main__":
    techniques = open("input.txt").read().strip().split("\n")
    cards = 119315717514047
    times = 101741582076661
    pos = 2020
    print(get_at_position(techniques, cards, times, pos))

