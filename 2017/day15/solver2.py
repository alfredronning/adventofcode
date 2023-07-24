def gen_a():
    val = 634
    while True:
        val = (val*16807)%2147483647
        if val%4 == 0:
            yield val

def gen_b():
    val = 301
    while True:
        val = (val*48271)%2147483647
        if val%8 == 0:
            yield val

if __name__ == "__main__":
    a = gen_a()
    b = gen_b()

    count = 0
    for _ in range(5_000_000):
        if (next(a)^next(b))&0xffff == 0:
            count += 1
    print(count)

