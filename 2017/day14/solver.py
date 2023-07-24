def knot_hash(input):
    lengths = [ord(c) for c in input]
    size = 256

    elements = [i for i in range(size)]

    current = 0
    skipsize = 0
    for _ in range(64):
        for length in lengths + [17, 31, 73, 47, 23]:
            if current + length < len(elements):
                sublist = elements[current:current+length]
                elements = elements[:current] + sublist[::-1] + elements[current+length:]
            else:
                cutoff = current + length - len(elements)
                sublist = elements[current:]+elements[:cutoff]
                elements = sublist[::-1][len(sublist)-cutoff:] + elements[cutoff:current] + sublist[::-1][:len(sublist)-cutoff]
            current = (current + length + skipsize) % len(elements)
            skipsize += 1

    res = ""
    for block in range(16):
        current = elements[block*16]
        for i in range(1, 16):
            current ^= elements[block*16+i]
        res += "{:02x}".format(current)
    return res

if __name__ == "__main__":
    inp = "amgozmfv"
    hashes = [knot_hash(inp+"-"+str(i)) for i in range(128)]
    used = 0

    for h in hashes:
        for c in h:
            used += "{:04b}".format(int(c, 16)).count("1")
    print(used)

