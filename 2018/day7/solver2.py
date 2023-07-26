from collections import defaultdict
if __name__ == "__main__":
    dependecies = open("input.txt").read().strip().split("\n")
    worker_count = 5
    working_time = 60

    dep_dict = defaultdict(list)
    steps = set(dep_dict)
    for dependency in dependecies:
        ds = dependency.split()
        a, b = ds[1], ds[7]
        steps.add(a)
        steps.add(b)
        dep_dict[b].append(a)

    steps = sorted(list(steps))
    order = ""
    workers = [0 for _ in range(worker_count)]
    working_on = {}
    time = 0
    while True:
        for i in range(len(workers)):
            if workers[i] == 1:
                order += working_on[i]
        workers = [t-1 if t>0 else 0 for t in workers]

        valid_steps = [s for s in steps if len([o for o in dep_dict[s] if o not in order]) == 0]
        while workers.count(0) and valid_steps:
            next_step = valid_steps[0]
            vacant_i = workers.index(0)
            workers[vacant_i] = working_time + ord(next_step) - ord("A") + 1
            working_on[vacant_i] = next_step
            steps.remove(next_step)
            valid_steps = [s for s in steps if len([o for o in dep_dict[s] if o not in order]) == 0]
        if not sum(workers):
            break
        time += 1
    print(time)

