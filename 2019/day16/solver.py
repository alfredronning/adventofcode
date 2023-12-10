if __name__ == "__main__":
    input = [int(i) for i in open("input.txt").read().strip()]
    base_pattern = [0, 1, 0, -1]
    for _ in range(100):
        next = []
        for n in range(len(input)):
            next_n = 0
            for j in range(len(input)):
                next_n += input[j]*base_pattern[(j+1)//(n+1)%4]
            next.append(abs(next_n)%10)
        input = next
    print("".join(str(i) for i in input[:8]))
