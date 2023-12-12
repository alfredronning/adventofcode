def find_checkspace_span(springs, counts):
    start = 0
    end = len(springs)
    for i in range(len(springs)):
        if springs[i] != ".":
            start = i
            break
    for i in range(start, len(springs)):
        if springs[i] == ".":
            end = i
            break
    end = min(end, (len(springs)-sum(counts[1:])-len(counts)+1)) # space needed to fit remainding groups
    return start, end

def find_possible_configurations(checkspace, count):
    remainders = []
    if "#" not in checkspace:
        for i in range(len(checkspace)-count+1):
            remainders.append("?"*i)
        return remainders
    for i in range(len(checkspace)-count+1):
        if "#" not in checkspace[:i] and (i+count == len(checkspace) or checkspace[i+count] == "?"):
            remainders.append(checkspace[i+count:])
    return remainders

def find_arrangements(springs, counts, cache):
    if (springs, tuple(counts)) in cache:
        return cache[(springs, tuple(counts))]
    if not counts:
        return "#" not in springs
    start, end = find_checkspace_span(springs, counts)
    if start >= end:
        return 0
    res = 0
    count = counts[0]
    checkspace = springs[start:end]
    if "#" not in checkspace:
        res += find_arrangements(springs[end:], counts, cache)
    possible_configurations = find_possible_configurations(checkspace, count)
    for remainder in possible_configurations:
        if not remainder and end < len(springs) and springs[end] == "#":
            continue
        res += find_arrangements((remainder+springs[end:])[1:], counts[1:], cache)
    cache[(springs, tuple(counts))] = res
    return res

if __name__ == "__main__":
    inp = [row.split() for row in  open("input.txt").read().strip().split("\n")]
    rows = []
    for springs, counts in inp:
        rows.append((((springs+"?")*5)[:-1], [int(i) for i in counts.split(",")]*5))
    res = 0
    for springs, counts in rows:
        res += find_arrangements(springs, counts, {})
    print(res)


