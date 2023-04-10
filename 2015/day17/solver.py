def find_combinations(eggnog, containers, visited):
    remainding_containers = [c for c in containers if c not in visited]
    if eggnog == 0:
        return 1
    if not len(remainding_containers):
        return 0
    next_container = remainding_containers[0]
    res = find_combinations(eggnog, containers, visited+[next_container])
    if eggnog >= next_container[1]:
        res += find_combinations(eggnog-next_container[1], containers, visited+[next_container])
    return res

if __name__ == "__main__":
    containers = [(i, int(v)) for i, v in enumerate(open("input.txt").read().strip().split("\n"))]
    eggnog = 150
    visited = []
    res = find_combinations(eggnog, containers, visited)
    print(res)

