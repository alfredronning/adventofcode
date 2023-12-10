if __name__ == "__main__":
    input = [int(i) for i in open("input.txt").read().strip()]*10000
    offset = int("".join(str(i) for i in input[:7]))
    input = input[offset:]
    for _ in range(100):
        next = []
        current_sum = 0
        for i in range(1, len(input)+1):
            current_sum = abs(current_sum + input[-i])%10
            next.append(current_sum)
        input = next[::-1]
    print("".join(str(i) for i in input[:8]))

