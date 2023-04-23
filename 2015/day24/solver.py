GROUPS = 2

def can_make_sum(packages, part_sum):
    if part_sum == 0:
        return True
    if part_sum < 0:
        return False
    for package in packages:
        if can_make_sum([p for p in packages if p != package], part_sum - package):
            return True
    return False


def can_split(packages):
    total_sum = sum(packages)
    if total_sum % GROUPS:
        return False
    part_sum = total_sum // GROUPS
    return can_make_sum(packages, part_sum)


def traverse(packages, picked, cache, lasti):
    if sum(packages) < GROUPS * sum(picked) or len(picked) > cache["lowest_grp"]:
        return
    elif sum(packages) == GROUPS * sum(picked):
        possible = can_split(packages)
        if possible:
            current_qe = 1
            for package in picked:
                current_qe *= package
            if len(picked) < cache["lowest_grp"] or current_qe < cache["lowest_qe"]:
                cache["lowest_grp"] = len(picked)
                cache["lowest_qe"] = current_qe
    else:
        for i in range(lasti, len(packages)):
            traverse(packages[:i] + packages[i + 1:], picked + [packages[i]], cache, i)


if __name__ == "__main__":
    packages = [int(p) for p in open("input.txt").read().strip().split("\n")[::-1]]

    cache = {"lowest_grp": float("inf"), "lowest_qe": float("inf")}
    traverse(packages, [], cache, 0)
    print(cache["lowest_qe"])
