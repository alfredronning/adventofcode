def find_mul(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 != n2 and n1 != n3 and n2 != n3 and n1+n2+n3 == 2020:
                    return n1*n2*n3

if __name__ == "__main__":
    numbers = [int(i) for i in open("input.txt").read().strip().split("\n")]
    print(find_mul(numbers))

