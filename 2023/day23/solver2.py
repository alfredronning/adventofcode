def find_choke_points(board, start, end):
    choke_point_neighbours = dict()
    queue_outer = [start]
    visited_outer = set()
    while queue_outer:
        current_choke_point = queue_outer.pop()
        choke_point_neighbours[current_choke_point] = []
        visited_outer.add(current_choke_point)
        queue_inner = [(current_choke_point, 0)]
        visited_inner = set()
        while queue_inner:
            current, dist = queue_inner.pop()
            visited_inner.add(current)
            if current == end:
                choke_point_neighbours[current_choke_point].append((end, dist))
            candidates = []
            for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    continue
                if board[nx][ny] == "#":
                    continue
                if (nx, ny) in visited_inner:
                    continue
                candidates.append((nx, ny))
            if not candidates:
                continue
            if len(candidates) == 1 or current == current_choke_point:
                for candidate in candidates:
                    queue_inner.append((candidate, dist+1))
            else:
                if (current, dist) not in choke_point_neighbours[current_choke_point]:
                    choke_point_neighbours[current_choke_point].append((current, dist))
                    if not current in visited_outer:
                        queue_outer.append(current)
    return choke_point_neighbours

def find_longest(choke_point_neighbours, start, end):
    queue = [(start, 0, [])]
    longest = 0
    while queue:
        current, current_len, path = queue.pop()
        if current == end:
            if current_len > longest:
                longest = current_len
                print(longest)
            continue
        for n, delta_dist in choke_point_neighbours[current]:
            if n in path:
                continue
            queue.append((n, current_len+delta_dist, path+[current]))
    return longest

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")
    start = (0, 1)
    end = (len(board)-1, len(board[0]) - 2)
    choke_point_neighbours = find_choke_points(board, start, end)
    print(find_longest(choke_point_neighbours, start, end))
