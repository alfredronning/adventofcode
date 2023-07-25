def test(n):
    for d in range(2, n):
        for e in range(2, n):
            if d*e==n:
                return True
    return False

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    count = 0
    for n in range(106700, 123701, 17):
        count += not is_prime(n)
    print(count)

