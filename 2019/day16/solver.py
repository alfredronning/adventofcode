if __name__ == "__main__":
    input = [int(i) for i in open("input.txt").read().strip()]
    for i in range(100):
        next = []
        for n in range(len(input)):
            pattern = [0]*(n+1)+[1]*(n+1)+[0]*(n+1)+[-1]*(n+1)
            pattern = pattern*(len(input)//len(pattern)+1)
            next_n = 0
            for j in range(len(input)):
                next_n += input[j]*pattern[j+1]
            next.append(int(str(next_n)[-1]))
        input = next
    print("".join(str(i) for i in input[:8]))
