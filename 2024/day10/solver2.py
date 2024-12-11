inp = [[int(i) for i in row] for row in open("input.txt").read().strip().split("\n")]

zeros = []

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 0:
            zeros.append((i, j))

def trailhead_score(board, head):
    visited = set(head)
    queue = [(head, 0, [head])]
    res = 0
    while queue:
        current_pos, current_val, trail = queue.pop()
        if current_val == 9:
            res += 1
            continue
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (current_pos[0] + d[0], current_pos[1] + d[1])
            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(inp) or next_pos[1] >= len(inp[0]):
                continue
            next_val = board[next_pos[0]][next_pos[1]]
            if next_val != current_val + 1:
                continue
            next_trail = trail + [next_pos]
            if tuple(next_trail) in visited:
                continue
            visited.add(tuple(next_trail))
            queue.append((next_pos, next_val, trail + [next_pos]))
    return res

res = sum(trailhead_score(inp, h) for h in zeros)

print(res)

