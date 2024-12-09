inp = open("input.txt").read().strip()

class Block:
    def __init__(self, id, startidx, len):
        self.id = id
        self.startidx = startidx
        self.len = len
        self.prev = None
        self.next = None

blocks = []

current_idx = 0
prev = None
for i, n in enumerate(inp):
    if n == "0":
        continue
    if i&1 == 0:
        current_block = Block(i//2, current_idx, int(n))
    else:
        current_block = Block(None, current_idx, int(n))
    current_block.prev = prev
    blocks.append(current_block)
    if prev is not None:
        prev.next = current_block
    prev = current_block
    current_idx += int(n)

def link_neighbours(current_block, blocks):
        if current_block.prev is None:
            current_block.next.prev = None
            return
        elif current_block.next is None:
            current_block.prev.next = None
            return
        current_block.prev.next = current_block.next
        current_block.next.prev = current_block.prev
        if current_block.prev.id is None and current_block.next.id is None:
            start_diff = current_block.next.startidx - current_block.prev.startidx
            current_block.next.startidx = current_block.prev.startidx
            current_block.next.len += start_diff
            current_block.next.prev = current_block.prev.prev
            blocks.remove(current_block.prev)

def attempt_move(current_block, blocks):
    for space_block in blocks:
        if space_block.id is not None or space_block.len < current_block.len or space_block.startidx > current_block.startidx:
            continue
        link_neighbours(current_block, blocks)
        current_block.prev = space_block.prev
        current_block.next = space_block
        current_block.startidx = space_block.startidx
        space_block.prev.next = current_block
        space_block.prev = current_block
        space_block.startidx += current_block.len
        space_block.len -= current_block.len
        return


for current_block in [b for b in blocks if b.id is not None][::-1]:
    attempt_move(current_block, blocks)

current_block = blocks[0]
res = 0
while current_block is not None:
    if current_block.id is not None:
        for i in range(current_block.len):
            res += current_block.id*(current_block.startidx+i)
    current_block = current_block.next

print(res)

