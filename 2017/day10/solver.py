if __name__ == "__main__":
    lengths = [int(i) for i in open("input.txt").read().strip().split(",")]
    size = 256

    elements = [i for i in range(size)]

    current = 0
    skipsize = 0
    for length in lengths:
        if current + length < len(elements):
            sublist = elements[current:current+length]
            elements = elements[:current] + sublist[::-1] + elements[current+length:]
        else:
            cutoff = current + length - len(elements)
            sublist = elements[current:]+elements[:cutoff]
            elements = sublist[::-1][len(sublist)-cutoff:] + elements[cutoff:current] + sublist[::-1][:len(sublist)-cutoff]
        current = (current + length + skipsize) % len(elements)
        skipsize += 1

    print(elements[0]*elements[1])

