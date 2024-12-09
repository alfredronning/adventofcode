inp = open("input.txt").read().strip()

blocks = []

id = 0
spaces = 0
for i, n in enumerate(inp):
    if i == "0":
        continue
    if i&1 == 0:
        blocks += [id]*int(n)
        id += 1
    else:
        blocks += [None]*int(n)
        spaces += int(n)

while spaces > 0:
    while blocks[-1] is None:
        blocks = blocks[:-1]
        spaces -= 1
    next_empty = blocks.index(None)
    blocks[next_empty] = blocks[-1]
    blocks = blocks[:-1]
    spaces -= 1

res = sum(i*n for i, n in enumerate(blocks))
print(res)

