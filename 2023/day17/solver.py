import heapq

def search(board, start, end):
    visited = dict()
    queue = [(0, start, (0, 0), 0)]
    while queue:
        heatloss, current, dir, dir_count = heapq.heappop(queue)
        if (current, dir, dir_count) in visited:
            continue
        visited[(current, dir, dir_count)] = heatloss 
        if current == end:
            return heatloss
        for d in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            if (-d[0], -d[1]) == dir:
                continue
            neighbour_dir_count = 1 if d != dir else dir_count + 1
            if neighbour_dir_count > 3:
                continue
            neighbour = current[0]+d[0], current[1]+d[1]
            if neighbour[0]>=0 and neighbour[1]>=0 and neighbour[0]<len(board) and neighbour[1]<len(board[0]):
                neighbour_heatloss = heatloss + board[neighbour[0]][neighbour[1]]
                heapq.heappush(queue, (neighbour_heatloss, neighbour, d, neighbour_dir_count)) # type: ignore

if __name__ == "__main__":
    board = [[int(i) for i in row] for row in open("input.txt").read().strip().split("\n")]
    print(search(board, (0, 0), ((len(board[0])-1, len(board[0])-1))))
