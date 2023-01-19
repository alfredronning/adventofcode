PREAMBLE = 25

if __name__ == "__main__":
    numbers = [int(i) for i in open("input.txt").read().strip().split("\n")]
    for i in range(PREAMBLE, len(numbers)):
        if not any(n1+n2 == numbers[i] for n1 in numbers[i-PREAMBLE:i] for n2 in numbers[i-PREAMBLE:i] if n1 != n2):
            print(numbers[i])

