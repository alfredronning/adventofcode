if __name__ == "__main__":
    inp = 3014387
    cyclic = {}
    for i in range(1, inp+1):
        cyclic[i] = i+1
    cyclic[inp] = 1

    current = 1
    while cyclic[current] != current:
        cyclic[current] = cyclic[cyclic[current]]
        current = cyclic[current]
    print(current)

