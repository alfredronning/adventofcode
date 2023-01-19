PREAMBLE = 25

def find_invalid(numbers):
    for i in range(PREAMBLE, len(numbers)):
        if not any(n1+n2 == numbers[i] for n1 in numbers[i-PREAMBLE:i] for n2 in numbers[i-PREAMBLE:i] if n1 != n2):
            return numbers[i]

if __name__ == "__main__":
    numbers = [int(i) for i in open("input.txt").read().strip().split("\n")]
    contageous = set()
    invalid = find_invalid(numbers)
    for i in range(len(numbers)):
        s = numbers[i]
        j = i+1
        while j < len(numbers):
            s += numbers[j]
            if s > invalid:
                break
            if s == invalid:
                for cont_id in range(i, j+1):
                    contageous.add(numbers[cont_id])
                break
            j += 1
    contageous = sorted(list(contageous))
    print(contageous[0]+contageous[-1])

