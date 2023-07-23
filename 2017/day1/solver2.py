if __name__ == "__main__":
    inp = open("input.txt").read().strip()

    print(sum(int(inp[i]) for i in range(len(inp)) if inp[i] == inp[(i+len(inp)//2)%len(inp)]))

