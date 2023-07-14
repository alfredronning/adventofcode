from copy import deepcopy

def get_connected_viable_pairs(node_dict, bound):
    viable_pairs = set()
    for node in node_dict:
        _, avail = node_dict[node]
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            n = (node[0] + d[0], node[1] + d[1])
            if n[0] < 0 or n[1] < 0 or n[0] > bound[0] or n[1] > bound[1]:
                continue
            used, _ = node_dict[n]
            if avail >= used and used > 0:
                viable_pairs.add((n, node))
    return list(viable_pairs)

def calc_hueristic(pair, data_location):
    score = pair[0][1]


def find_shortest(node_dict, bound, steps, cache, data_location):
    if data_location == (0, 0):
        cache["best"] = steps
        return steps
    if steps + 1 >= cache["best"]:
        return float("inf")

    h = hash(tuple(node_dict.items()))
    if h in cache["visited"]:
        if cache["visited"][h] <= steps:
            return float("inf")

    cache["visited"][h] = steps

    viable_pairs = get_connected_viable_pairs(node_dict, bound)


    for from_n, to_n in viable_pairs:
        next_node_dict = deepcopy(node_dict)
        data = node_dict[from_n][0]
        next_node_dict[to_n] = (node_dict[to_n][0] + data, node_dict[to_n][1] - data)
        next_node_dict[from_n] = (0, node_dict[from_n][1] + data)

        if from_n == data_location:
            next_data_location = to_n
        else:
            next_data_location = data_location

        find_shortest(next_node_dict, bound, steps + 1, cache, next_data_location)


if __name__ == "__main__":
    nodes = open("input.txt").read().strip().split("\n")
    bound = (36, 26)

    #nodes = open("testinput.txt").read().strip().split("\n")
    #bound = [2, 2]

    node_dict = dict()
    for node in nodes[2:]:
        fs, _, used, avail, _ = node.split()
        x = int(fs.split("-")[1][1:])
        y = int(fs.split("-")[2][1:])
        node_dict[(x, y)] = (int(used[:-1]), int(avail[:-1]))
    del nodes

    #cache = {"best": 7, "visited": dict()}
    for row in range(bound[0]+1):
        r = ""
        for col in range(bound[1]+1):
            if col == 0 and row == 36:
                n = "  G  "
            elif col == 0 and row == 0:
                n = " (0) "
            else:
                node = node_dict[(row,col)]
                #print(node[0])
                if node[0] > 100:
                    n = "  #  "
                elif node[0] == 0:
                    n = "  _  "
                else:
                    n = "  .  "
            r += n + " "*(8-len(n))
        print(r)
        r = ""

    #find_shortest(node_dict, bound, 0, cache, (0, 26))
    #print(cache["best"])kkk
