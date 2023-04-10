def find_combinations(eggnog, containers, visited, cache, containers_used):
    remainding_containers = [c for c in containers if c not in visited]
    if containers_used > cache["min_containers"]:
        return
    if eggnog == 0:
        if containers_used == cache["min_containers"]:
            cache["container_amount"] += 1
        else:
            cache["min_containers"] = containers_used
            cache["container_amount"] = 1
        return
    if not len(remainding_containers):
        return
    next_container = remainding_containers[0]
    find_combinations(eggnog, containers, visited+[next_container], cache, containers_used)
    if eggnog >= next_container[1]:
        find_combinations(eggnog-next_container[1], containers, visited+[next_container], cache, containers_used+1)

if __name__ == "__main__":
    containers = [(i, int(v)) for i, v in enumerate(open("input.txt").read().strip().split("\n"))]
    eggnog = 150
    visited = []
    cache = {"min_containers": float("inf"), "container_amount": 0}
    find_combinations(eggnog, containers, visited, cache, 0)
    print(cache)

