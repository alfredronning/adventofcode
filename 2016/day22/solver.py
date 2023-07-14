def count_connected_viable_pairs(node_dict, bound):
    viable_pairs = set()
    for node in node_dict:
        _, _, avail, _ = node_dict[node]
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            n = (node[0]+d[0], node[1]+d[1])
            if n[0]<0 or n[1]<0 or n[0]>bound[0] or n[1]>bound[1]:
                continue
            _, used, _, _ = node_dict[node]
            if avail >= used and used > 0:
                viable_pairs.add(tuple(sorted((node, n))))
    return len(viable_pairs)

def count_viable_pairs(node_dict, bound):
    viable_pairs = set()
    for node in node_dict:
        _, _, avail, _ = node_dict[node]
        for n in node_dict:
            if node == n:
                continue
            _, used, _, _ = node_dict[n]
            if avail >= used and used > 0:
                viable_pairs.add(tuple(sorted((node, n))))
    return len(viable_pairs)


if __name__ == "__main__":
    nodes = open("input.txt").read().strip().split("\n")
    bound = [36, 26]

    node_dict = dict()
    for node in nodes[2:]:
        fs, size, used, avail, use = node.split()
        x = int(fs.split("-")[1][1:])
        y = int(fs.split("-")[2][1:])
        node_dict[(x, y)] = (int(size[:-1]), int(used[:-1]), int(avail[:-1]), int(use[:-1]))
    print(count_viable_pairs(node_dict, bound))

