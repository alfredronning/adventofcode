def print_board(lumber_yards, trees, open, min_x, min_y, max_x, max_y):
    print("-------------------------------------------------------")
    for i in range(min_x, max_x+1):
        row = ""
        for j in range(min_y, max_y+1):
            if (i, j) in lumber_yards:
                row += "#"
            elif (i, j) in trees:
                row += "|"
            elif (i, j) in open:
                row += "."
            else:
                raise Exception("void tile")
        print(row)
    print("-------------------------------------------------------")


if __name__ == "__main__":
    acres = open("input.txt").read().strip().split("\n")
    minutes = 10
    lumber_yards = set()
    trees = set()
    open = set()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    min_x = min_y = float("inf")
    max_x = max_y = 0

    for i, line in enumerate(acres):
        for j, tile in enumerate(line):
            if tile == "#":
                lumber_yards.add((i, j))
            elif tile == "|":
                trees.add((i, j))
            elif tile == ".":
                open.add((i, j))
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

    for i in range(minutes):
        #print_board(lumber_yards, trees, open, min_x, min_y, max_x, max_y)
        next_lumber_yards = set()
        next_trees = set()
        next_open = set()

        for o in open:
            tree_count = 0
            for d in directions:
                neighbour = (o[0]+d[0], o[1]+d[1])
                if neighbour in trees:
                    tree_count += 1
            if tree_count >= 3:
                next_trees.add(o)
            else:
                next_open.add(o)
        for t in trees:
            lumberyard_count = 0
            for d in directions:
                neighbour = (t[0]+d[0], t[1]+d[1])
                if neighbour in lumber_yards:
                    lumberyard_count += 1
            if lumberyard_count >= 3:
                next_lumber_yards.add(t)
            else:
                next_trees.add(t)
        for l in lumber_yards:
            lumberyard_count = 0
            tree_count = 0
            for d in directions:
                neighbour = (l[0]+d[0], l[1]+d[1])
                if neighbour in lumber_yards:
                    lumberyard_count += 1
                if neighbour in trees:
                    tree_count += 1
            if lumberyard_count and tree_count:
                next_lumber_yards.add(l)
            else:
                next_open.add(l)
        lumber_yards = next_lumber_yards
        trees = next_trees
        open = next_open

    print(len(lumber_yards),len(trees))
    print(len(lumber_yards)*len(trees))

