class Blueprint:
    def __init__(self, blueprint):
        robots = blueprint.split(":")[1].split(".")[:-1]
        self.prices = [self.findcost(robot) for robot in robots]
        self.max_cost = [max(self.prices[i][j] for i in range(4)) for j in range(4)]

    def findcost(self, robot):
        price = [0, 0, 0, 0]
        costs = robot.split("robot costs ")[1].split()
        while True:
            amount = int(costs.pop(0))
            currency = costs.pop(0)
            if currency == "ore":
                price[0] = amount
            elif currency == "clay":
                price[1] = amount
            elif currency == "obsidian":
                price[2] = amount
            else:
                price[3] = amount
            if not costs:
                break
            costs.pop(0)
        return price

    def can_afford(self, i, ores):
        return all(ores[j] >= self.prices[i][j] for j in range(4))

    def buy(self, i, ores):
        return [ores[j]-self.prices[i][j] for j in range(4)]

def find_best(blueprint, ores, could_afford, robots, building, time, cache):
    if time <= 0:
        return ores[-1]
    robots = [robots[i]+(1 if building == i else 0) for i in range(4)]
    # return 0 if it can't beat the max
    if ores[-1] + (robots[-1] + time) * time <= cache["max"]:
        return 0
    # return same value if the exact state is reached before
    if (tuple(ores), tuple(robots)) in cache:
        return cache[(tuple(ores), tuple(robots))]
    ores_next = [ores[i]+robots[i] for i in range(4)]
    can_afford = [blueprint.can_afford(i, ores) for i in range(4)]
    # always buy blueprint if possible
    if can_afford[3]:
        return find_best(blueprint, blueprint.buy(3, ores_next), can_afford, robots, 3, time-1, cache)
    best = 0
    if not (could_afford[0] and building == -1) and can_afford[0]:
        # do not expand branch if there is no time to profit from it
        if time > blueprint.prices[0][0]:
            # don't make more robots than the max orecount one can spend on robots
            if robots[0] < blueprint.max_cost[0]:
                best = max(best, find_best(blueprint, blueprint.buy(0, ores_next), can_afford, robots, 0, time-1, cache))
    if not (could_afford[1] and building == -1) and can_afford[1]:
        if time > blueprint.prices[1][1]:
            if robots[1] < blueprint.max_cost[1]:
                best = max(best, find_best(blueprint, blueprint.buy(1, ores_next), can_afford, robots, 1, time-1, cache))
    if not (could_afford[2] and building == -1) and can_afford[2]:
        if time > blueprint.prices[2][2]:
            if robots[2] < blueprint.max_cost[2]:
                best = max(best, find_best(blueprint, blueprint.buy(2, ores_next), can_afford, robots, 2, time-1, cache))
    best = max(best, find_best(blueprint, ores_next, can_afford, robots, -1, time-1, cache))
    cache[(tuple(ores), tuple(robots))] = best
    if best > cache["max"]:
        cache["max"] = best
    return best

def part1(blueprints):
    total = 0
    for i, blueprint in enumerate(blueprints):
        ores = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        can_afford = [False]*4
        bought = -1
        time = 24
        cache = {}
        cache["max"] = 0
        res = find_best(blueprint, ores, can_afford, robots, bought, time, cache)
        total += (i+1) * res
    return total

def part2(blueprints):
    total = 1
    for i, blueprint in enumerate(blueprints):
        ores = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        can_afford = [False]*4
        bought = -1
        time = 32
        cache = {}
        cache["max"] = 0
        res = find_best(blueprint, ores, can_afford, robots, bought, time, cache)
        total *= res
    return total


if __name__ == "__main__":
    blueprints = open("input.txt").read().strip().split("\n")
    blueprints = [Blueprint(o) for o in blueprints]
    print(part1(blueprints))
    print(part2(blueprints[:3]))
