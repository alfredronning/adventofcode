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

def traverse(grid, current, visited):
    queue = [current]
    while queue:
        current = queue.pop()
        visited.add(current)
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n[0] < 0 or n[0] >= 128 or n[1] < 0 or n[1] >= 128:
                continue
            if n in visited or grid[n[0]][n[1]] == "0":
                continue
            queue.append(n)

if __name__ == "__main__":
    inp = "amgozmfv"
    hashes = [knot_hash(inp+"-"+str(i)) for i in range(128)]

    grid = []
    for h in hashes:
        row = ""
        for c in h:
            row += "{:04b}".format(int(c, 16))
        grid.append(row)

    visited = set()
    regions = 0
    for i in range(128):
        for j in range(128):
            if (i, j) in visited or grid[i][j] == "0":
                continue
            traverse(grid, (i, j), visited)
            regions += 1

    print(regions)


